import datetime
import random
from src.interface.energy_repository_inte import EnergyRepositoryInterface
from src.interface.example_repository_inte import ExampleRepositoryInterface
from src.entity.energy_generation_enti import EnergyGeneration
from src.entity.energy_usage_enti import EnergyUsage

# Template factor per month:
monthly_solar_activity_factor = (
    0.08, 0.22, 0.45, 0.6, 0.78, 1, 0.82, 0.76, 0.72, 0.68, 0.2, 0.04)
# Template factor per hour:
daily_solar_activity_factor = (
    0, 0, 0, 0.005, 0.020, 0.038, 0.056, 0.07, 0.08, 0.09, 0.095, 0.1, 0.095, 0.09, 0.08, 0.07, 0.056, 0.03, 0.020, 0.005, 0, 0, 0, 0)
kvp_factor = 1500


def generate_periodical_data(time_to, site_id, kvp):
    diff_minutes = 5
    thirty_days_munutes = 43200
    time_from = time_to - datetime.timedelta(minutes=diff_minutes)
    time_to_str = time_to.strftime(f"%Y-%m-%d %H:%M:%S")
    time_from_str = time_from.strftime(f"%Y-%m-%d %H:%M:%S")
    # Emulate energy generation:
    month_int = int(time_from.strftime(f"%m"))
    hour_int = int(time_from.strftime(f"%H"))
    # Calculate daily energy:
    daily_total_energy = kvp * kvp_factor * \
        monthly_solar_activity_factor[month_int]
    daily_hour_factor = daily_solar_activity_factor[hour_int]
    # Generate test energy value daily energy random +/-20% * get hour total energy with hour factor and take the minutes factor)
    generated_energy = int(
        daily_total_energy * random.uniform(0.8, 1.2) * daily_hour_factor * diff_minutes/60)

    return EnergyGeneration(
        from_time=time_from_str,
        to_time=time_to_str,
        site_id=site_id,
        energy=generated_energy
    )


def usage_periodical_data(time_to, site_id, kw_max):
    diff_minutes = 5
    thirty_days_munutes = 43200
    time_from = time_to - datetime.timedelta(minutes=diff_minutes)
    time_to_str = time_to.strftime(f"%Y-%m-%d %H:%M:%S")
    time_from_str = time_from.strftime(f"%Y-%m-%d %H:%M:%S")
    # Emulate energy usage:
    hour_int = int(time_from.strftime(f"%H"))
    max_power = int(kw_max * 0.2)
    if 7 <= hour_int <= 23:
        max_power = kw_max

    # Generate test energy value daily energy random +/-20% * get hour total energy with hour factor and take the minutes factor)
    used_energy = int(random.uniform(0.8, 1.0) * max_power)

    return EnergyGeneration(
        from_time=time_from_str,
        to_time=time_to_str,
        site_id=site_id,
        energy=used_energy
    )


class MockRepository(ExampleRepositoryInterface, EnergyRepositoryInterface):
    def __init__(self, RETURN_STRING):
        self.ng = RETURN_STRING

    def example(self, data):
        return "Here is example_repository for ExampleUseCase"

    def example_sqlite(self, data):
        return "Here is empty example_sqlite_repository for ExampleSqliteUseCase"

    def energy_generation(self, data) -> EnergyGeneration:
        results = []
        # Generate for range of time:
        if "from_time" in data:
            time_to = datetime.datetime.strptime(
                data["to_time"], f"%Y-%m-%d %H:%M:%S")
            time_from = datetime.datetime.strptime(
                data["from_time"], f"%Y-%m-%d %H:%M:%S")
            time_diff = time_to - time_from
            # Generate data for every 5 minutes (300s):
            time_next = time_from
            for i in range(int(time_diff.total_seconds()/300)):
                time_next
                results.append(generate_periodical_data(
                    time_to=time_next, site_id=data["site_id"], kvp=data["kvp"]))
                time_next = time_next + datetime.timedelta(minutes=5)
            return results
        # Generate current 5 minutes:
        else:
            time_to = datetime.datetime.now()
            results.append(generate_periodical_data(
                time_to=time_to, site_id=data["site_id"], kvp=data["kvp"]))
            return results

    def energy_usage(self, data) -> EnergyUsage:
        results = []
        # Generate for range of time:
        if "from_time" in data:
            time_to = datetime.datetime.strptime(
                data["to_time"], f"%Y-%m-%d %H:%M:%S")
            time_from = datetime.datetime.strptime(
                data["from_time"], f"%Y-%m-%d %H:%M:%S")
            time_diff = time_to - time_from
            # Generate data for every 5 minutes (300s):
            time_next = time_from
            for i in range(int(time_diff.total_seconds()/300)):
                time_next
                results.append(generate_periodical_data(
                    time_to=time_next, site_id=data["site_id"], kvp=data["kw_max"]))
                time_next = time_next + datetime.timedelta(minutes=5)
            return results
        # Generate current 5 minutes:
        else:
            time_to = datetime.datetime.now()
            results.append(generate_periodical_data(
                time_to=time_to, site_id=data["site_id"], kvp=data["kw_max"]))
            return results

    def current_usage(self,data):
        return "current_usage - not used with repository"

    def current_generation(self,data):
        return "current_generation - not used with repository"

