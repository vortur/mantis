from argparse import OPTIONAL
from typing import Optional
import logging

from codegen.stringcase import camel_case
from codegen.stringcase import snake_case


def find_in_file(file_path, search_str):
    try:
        with open(file_path) as f:
            if search_str in f.read():
                return True
            else:
                return False
    except FileNotFoundError as e:
        return False


def check_file_exist(file_path):
    try:
        with open(file_path) as f:
            return True
    except FileNotFoundError as e:
        return False


def usecase_gen(build_path, method_str, interface_str):
    logger = logging.getLogger('Usecase Generator')
    logger.setLevel('DEBUG')

    class_name_str = camel_case(method_str) + 'UseCase'
    func_name_str = snake_case(method_str)
    class_interface_str = camel_case(interface_str)
    interface_name_str = snake_case(interface_str)

    # Create new usecase:
    try:
        with open('./codegen/templates/usecase.tpl', 'r') as tmp:
            usecase_path = build_path + 'usecase/' + method_str + '_usec.py'
            logger.info("Generating UseCase: " + usecase_path)
            # Check if there is no same usecase:
            if find_in_file(usecase_path, class_name_str):
                raise Exception('UseCase exists!', class_name_str)

            with open(usecase_path, 'w') as fout:
                for line in tmp:
                    updated_line = line.replace(
                        '$classUseCase', class_name_str)
                    updated_line = updated_line.replace(
                        '$methodUseCase', func_name_str)
                    fout.write(updated_line)
                fout.close()
        tmp.close()
    except Exception as e:
        logger.warning(e)

    # Create new REST config:
    try:
        with open('./codegen/templates/rest.tpl', 'r') as tmp:
            rest_path = build_path + 'rest/' + method_str + '_rest.py'
            logger.info("Generating REST config: " + rest_path)
            # Check if there is no same REST config:
            if find_in_file(rest_path, class_name_str):
                raise Exception('REST config exists!', class_name_str)

            with open(rest_path, 'w') as fout:
                for line in tmp:
                    updated_line = line.replace(
                        '$classUseCase', class_name_str)
                    updated_line = updated_line.replace(
                        '$methodUseCase', func_name_str)
                    fout.write(updated_line)
                fout.close()
        tmp.close()
    except Exception as e:
        logger.warning(e)

    # Add new flask endpoint route:
    try:
        with open('./codegen/templates/flask_entry.tpl', 'r') as tmp:
            with open('./codegen/templates/flask_import_entry.tpl', 'r') as imp_tmp:
                new_flask_line = []
                flask_path = build_path + '../app.py'
                logger.info("Inserting new flask route: " + flask_path)
                # Check if there is no same Flask route:
                if find_in_file(flask_path, 'rom src.rest.{}_rest import'.format(func_name_str)):
                    raise Exception('Flask route exists!', func_name_str)

                with open(flask_path, 'r') as fin:
                    for line in fin:
                        if 'if __name__' in line:
                            for entry in tmp:
                                updated_line = entry.replace(
                                    '$classUseCase', class_name_str)
                                updated_line = updated_line.replace(
                                    '$methodUseCase', func_name_str)
                                new_flask_line.append(updated_line)
                        new_flask_line.append(line)
                        if '#Below generated imports' in line:
                            for entry in imp_tmp:
                                updated_line = entry.replace(
                                    '$classUseCase', class_name_str)
                                updated_line = updated_line.replace(
                                    '$methodUseCase', func_name_str)
                                new_flask_line.append(updated_line)
                    fin.close()

                with open(flask_path, 'w') as fout:
                    for line in new_flask_line:
                        fout.writelines(line)
                    fout.close()
            imp_tmp.close()
        tmp.close()
    except Exception as e:
        logger.warning(e)

    # Update/Create repository interface:
    try:
        interface_path = build_path + 'interface/' + \
            interface_name_str + '_repository_inte.py'
        # Check if interface exists (do we need to create new one):
        if check_file_exist(interface_path):
            # Update interface:
            with open('./codegen/templates/interface_entry.tpl', 'r') as tmp:
                logger.info("Updating repository interface: " + interface_path)
                # Check if there is no same repository interface entry:
                if find_in_file(interface_path, 'def {}('.format(func_name_str)):
                    raise Exception(
                        'Interface entry exists!', func_name_str)

                with open(interface_path, 'a') as fout:
                    for entry in tmp:
                        updated_line = entry.replace(
                            '$classUseCase', class_name_str)
                        updated_line = updated_line.replace(
                            '$methodUseCase', func_name_str)
                        fout.writelines(updated_line)
                    fout.close()
            tmp.close()
        else:
            # Create interface:
            with open('./codegen/templates/interface_repo.tpl', 'r') as tmp:
                with open(interface_path, 'w') as fout:
                    for entry in tmp:
                        updated_line = entry.replace(
                            '$interface', class_interface_str)
                        updated_line = updated_line.replace(
                            '$methodUseCase', func_name_str)
                        fout.writelines(updated_line)
                    fout.close()
                tmp.close
            # Add interface to Mock:
            new_interface_line = []
            new_interface_line.append('from src.interface.{}_repository_inte import {}RepositoryInterface\n'.format(
                interface_name_str, class_interface_str))
            mock_path = build_path + 'repository/mock_repo.py'
            with open(mock_path, 'r') as fin:
                for line in fin:
                    if 'class MockRepository' in line:
                        # Insert new interface at the end of Mock Interfaces - before the ...):
                        replace_line = '{}, {}RepositoryInterface):\n'.format(line.split(')')[0], class_interface_str)
                        new_interface_line.append(replace_line)
                    else:
                        new_interface_line.append(line)
                fin.close()

            with open(mock_path, 'w') as fout:
                for line in new_interface_line:
                    fout.writelines(line)
                fout.close()
    except Exception as e:
        logger.warning(e)

    # Update mock repository:
    try:
        with open('./codegen/templates/mock_entry.tpl', 'r') as tmp:
            mock_path = build_path + 'repository/mock_repo.py'
            logger.info("Updating mock repository: " + mock_path)
            # Check if there is no same mock repository method:
            if find_in_file(mock_path, 'def {}('.format(func_name_str)):
                raise Exception('Repository mock entry exists!', func_name_str)

            with open(mock_path, 'a') as fout:
                for entry in tmp:
                    updated_line = entry.replace(
                        '$classUseCase', class_name_str)
                    updated_line = updated_line.replace(
                        '$methodUseCase', func_name_str)
                    fout.writelines(updated_line)
                fout.close()
        tmp.close()
    except Exception as e:
        logger.warning(e)

    # Create new unit test:
    try:
        with open('./codegen/templates/test_usecase.tpl', 'r') as tmp:
            rest_path = build_path + '../tests/usecase/test_' + method_str + '.py'
            logger.info("Generating UnitTest: " + rest_path)
            # Check if there is no same UnitTest:
            if find_in_file(rest_path, class_name_str):
                raise Exception('UnitTest usecase exists!', class_name_str)

            with open(rest_path, 'w') as fout:
                for line in tmp:
                    updated_line = line.replace(
                        '$classUseCase', class_name_str)
                    updated_line = updated_line.replace(
                        '$methodUseCase', func_name_str)
                    fout.write(updated_line)
                fout.close()
        tmp.close()
    except Exception as e:
        logger.warning(e)

    # Update test mock repository:
    try:
        with open('./codegen/templates/test_repo.tpl', 'r') as tmp:
            mock_path = build_path + '../tests/repository/test_mock_repo.py'
            logger.info("Updating test mock repository: " + mock_path)
            # Check if there is no same test mock repository method:
            if find_in_file(mock_path, 'def test_{}('.format(func_name_str)):
                raise Exception(
                    'UnitTest mock repository entry exists!', func_name_str)

            with open(mock_path, 'a') as fout:
                for entry in tmp:
                    updated_line = entry.replace(
                        '$classUseCase', class_name_str)
                    updated_line = updated_line.replace(
                        '$methodUseCase', func_name_str)
                    fout.writelines(updated_line)
                fout.close()
        tmp.close()
    except Exception as e:
        logger.warning(e)
