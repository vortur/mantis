import sys
import logging
import argparse


from codegen.usecase_gen import usecase_gen
from codegen.entity_gen import entity_gen


def main(args=None):
    LOGFORMAT = "%(asctime)s - %(name)s - [%(process)d/%(threadName)-10s] %(levelname)-8s \"%(filename)s/%(funcName)s:%(lineno)d\" \"%(message)s\""
    logging.basicConfig(format=LOGFORMAT)
    build_path = './src/'

    if args is None:
        args = sys.argv[1:]

    # Instantiate the parser
    parser = argparse.ArgumentParser(
        description='Domain Driven Development structure generator.',
        usage='python3 -m codegen -u my_example -i examples')
    parser.add_argument('-e', '--entity', help='name of the entity')
    parser.add_argument('-u', '--usecase', help='name of the uscase in snake_case must be used with -i (interface)')
    parser.add_argument('-i', '--interface', help='name of the interface in snake_case must be used with -u (usecase)')
    args = parser.parse_args()

    if args.usecase and args.interface:
        print("usecase: {} and interface: {}".format(args.usecase,args.interface))
        usecase_gen(build_path, args.usecase, args.interface)
    elif args.entity:
        print("entity is set: ", args.entity)
        entity_gen(args.entity, build_path)
    elif bool(args.usecase) ^ bool(args.interface):
        print("wrong parameters... uscase must be generated with interface, cant use them separately, type -h for help")
    else:
        print("wrong parameters... type -h for help")


if __name__ == "__main__":
    sys.exit(main())
