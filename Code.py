import matplotlib.pyplot as plt
import random

CHILDREN = 1
ADULT = 2
SENIER_CITIZEN = 3

CITIZEN_INDEX = 0


class Community:
    population = 1000000
    senier_citizen_percent = random.randint(31, 40)
    adult_percent = 100 - senier_citizen_percent - 20

    max_adult = int(population * adult_percent / 100)
    max_children = int(population * 20 / 100)
    max_senier_citizen = int(population * senier_citizen_percent / 100)

    adults_with_family = 0
    children_with_family = 0
    senier_citizen_with_family = 0

    all_citizens = []


class Covid:
    infected = []
    hospitalized = []
    fatalities = []
    recovered = []
    facemask_policy = False
    travel_restriction_enforcement = False


class Day:
    day_number = 0
    infected = 0
    hospitalized = 0
    fatalities = 0
    recovered = 0


class Citizen:
    is_infected = 0
    citizen_id = 0
    hospitalized_days = 0
    is_hospitalized = False
    is_alive = 0
    number_of_days_infected = 0
    is_family_infected = 0
    is_in_essensial_service = False
    is_recovered = False

    def __init__(self, type, ability_to_infect, family_id):
        global CITIZEN_INDEX
        self.citizen_id = CITIZEN_INDEX
        CITIZEN_INDEX = CITIZEN_INDEX + 1
        self.type = type
        self.ability_to_infect = ability_to_infect
        self.family_id = family_id


def make_families():
    # print(Community.adults_with_family)
    # print(Community.senier_citizen_with_family)
    # print(Community.children_with_family)

    for family_id in range(1, 100001):
        Community.all_citizens.append(Citizen(ADULT, range(15, 41), family_id))
        Community.all_citizens.append(Citizen(CHILDREN, range(10, 21), family_id))
        Community.children_with_family += 1
        Community.adults_with_family += 1

        other_family_member_count = random.randint(0, 5)
        # print(f" Family {family_id} success {other_family_member_count} ")
        if other_family_member_count > 0:

            if Community.max_senier_citizen > Community.senier_citizen_with_family:
                senier_citizens = random.randint(0, other_family_member_count)
                # print(f"random count senier {senier_citizens}")
                exceded_diff = Community.senier_citizen_with_family + senier_citizens - Community.max_senier_citizen
                if exceded_diff > 0:
                    senier_citizens -= exceded_diff
                for _ in range(senier_citizens):
                    Community.all_citizens.append(Citizen(SENIER_CITIZEN, range(35, 61), family_id))
                Community.senier_citizen_with_family += senier_citizens
                other_family_member_count -= senier_citizens

            if Community.max_children > Community.children_with_family:
                childrens = random.randint(0, other_family_member_count)
                # print(f"random count children{childrens}")
                exceded_diff = Community.children_with_family + childrens - Community.max_children
                if exceded_diff > 0:
                    childrens -= exceded_diff
                for _ in range(childrens):
                    Community.all_citizens.append(Citizen(CHILDREN, range(10, 21), family_id))
                Community.children_with_family += childrens
                other_family_member_count -= childrens

            if Community.max_adult > Community.adults_with_family:
                adult = other_family_member_count
                # print(f"adults in this family {adult}")
                exceded_diff = Community.adults_with_family + adult - Community.max_adult
                if exceded_diff > 0:
                    adult -= exceded_diff
                for _ in range(adult):
                    Community.all_citizens.append(Citizen(ADULT, range(15, 41), family_id))
                Community.adults_with_family += adult

    # print(f"\n\nAdults with family {Community.adults_with_family} ")
    # print(f"Senier citizen with family {Community.senier_citizen_with_family} ")
    # print(f"Children with family {Community.children_with_family}")
    # print(f"All Family citizens {len(Community.all_citizens)}\n")
    #
    # print(f"Adults without family {Community.max_adult - Community.adults_with_family}")
    # print(f"Senier citizen without family {Community.max_senier_citizen - Community.senier_citizen_with_family}")
    # print(f"Children without family {Community.max_children - Community.children_with_family}")


def fill_others():
    # others are orphans their family id is zero
    for _ in range(Community.max_adult - Community.adults_with_family):
        Community.all_citizens.append(Citizen(ADULT, range(15, 41), 0))
    for _ in range(Community.max_children - Community.children_with_family):
        Community.all_citizens.append(Citizen(CHILDREN, range(10, 21), 0))
    for _ in range(Community.max_senier_citizen - Community.senier_citizen_with_family):
        Community.all_citizens.append(Citizen(SENIER_CITIZEN, range(35, 61), 0))
    # orphans_count = 0
    # for person in Community.all_citizens:   finding orphans
    #     if person.family_id == 0 :
    #         orphans_count +=1
    # print(f"orphans_count  =  {orphans_count}")


def set_essensial_service_people():
    essensial_service_adults = 0
    for person in Community.all_citizens:
        if person.type == ADULT:
            person.is_in_essensial_service = True
            essensial_service_adults += 1
        if essensial_service_adults == 40000:
            break
    essensial_service_adults = 0
    for person in Community.all_citizens:
        if (person.type == ADULT) & (person.is_in_essensial_service == True):
            essensial_service_adults += 1
    # print(f"Essential serv peoples {essensial_service_adults}")


def draw_charts(days_list):
    days = []
    infected_count = []
    fatality_count = []
    hospitalized_count = []
    recovered_count = []
    for each_day in days_list:
        days.append(each_day.day_number)
        infected_count.append(each_day.infected)
        fatality_count.append(each_day.fatalities)
        hospitalized_count.append(each_day.hospitalized)
        recovered_count.append(each_day.recovered)

    # plotting graphs

    fig, axs = plt.subplots(4)
    axs[0].plot(days, infected_count)
    axs[0].set_title('Infections')
    axs[1].plot(days, hospitalized_count, 'tab:orange')
    axs[1].set_title('Hospitalizations')
    axs[2].plot(days, recovered_count, 'tab:green')
    axs[2].set_title('Recoveries')

    axs[3].plot(days, fatality_count, 'tab:red')
    axs[3].set_title('Deaths')
    # fig.tight_layout()
    for ax in axs.flat:
        ax.set(xlabel='Days', ylabel='No. of Citizens')

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    plt.show()


def infect():
    days_list = []
    print("+------------------------+")
    print("|    Covid Simulation    |")
    print("+------------------------+")

    # all covid cases
    total_covid_cases = 0
    citizen_number = 0
    has_family = False
    while has_family is False:
        random_number = random.randint(1, 1000000) - 1
        if Community.all_citizens[random_number].family_id > 0:
            has_family = True
            citizen_number = random_number

    # print(f"Citizen Count : {len(Community.all_citizens)}")
    # print(citizen_number)

    Community.all_citizens[citizen_number].is_infected = True
    first_day = Day()
    first_day.infected = 1
    first_day.day_number = 1
    first_day.fatalities = 0
    first_day.recovered = 0
    first_day.hospitalized = 0
    days_list.append(first_day)

    total_covid_cases = total_covid_cases + 1
    Covid.infected.append(Community.all_citizens[citizen_number])

    # Community.all_citizens[citizen_number + 10].is_infected = True
    # Covid.infected.append(Community.all_citizens[citizen_number + 10])

    # print(f"Citizen ge : {Community.all_citizens[citizen_number].is_infected}")
    all_infected_families = []
    inf_list = []

    previous_death_count = 0
    # inf_list.append(Community.all_citizens[citizen_number])
    for day in range(2, 51):
        # day's covid cases
        covid_cases_for_day = 0
        print("+------------------------+")
        print(f"|    Day Count : {day}     |")
        print("+------------------------+")
        # infecting family
        infected_id = []
        for citizen in Community.all_citizens:
            if citizen.is_infected and citizen.family_id > 0 and not citizen.is_family_infected:

                if citizen.family_id not in infected_id:
                    infected_id.append(citizen.family_id)
                    all_infected_families.append(citizen.family_id)

        for id in infected_id:
            family_members = []
            for citizen in Community.all_citizens:
                if citizen.family_id is id:
                    family_members.append(citizen)

            # print(f"family length : {len(family_members)}")
            infect_probability = random.randint(40, 80)
            person_infect_count = random.randint(0, 100)
            if person_infect_count <= infect_probability:
                for each_member in family_members:
                    each_member.is_family_infected = True
                # citizen.is_family_infected = True

                if family_members[0].is_infected:
                    family_members[1].is_infected = True
                    total_covid_cases = total_covid_cases + 1
                    covid_cases_for_day = covid_cases_for_day + 1
                    Covid.infected.append(family_members[1])
                    inf_list.append(family_members[1])
                else:
                    family_members[0].is_infected = True
                    Covid.infected.append(family_members[0])
                    inf_list.append(family_members[0])
                    total_covid_cases = total_covid_cases + 1
                    covid_cases_for_day = covid_cases_for_day + 1

        # infect the community
        # print(f"Covid.indected length : {len(Covid.infected)}")
        for infected_person in Covid.infected:
            infected_ability_days = random.randint(5, 11)
            infect_chance = random.randint(0, 100)
            if not infected_person.is_hospitalized and infect_chance > 40:
                # print(f"Person id : {infected_person.citizen_id} + {infected_person.number_of_days_infected}")

                if Covid.facemask_policy is False and Covid.travel_restriction_enforcement is False:
                    # print("Facemask policy disabled | Travel restictions disabled")
                    range_begin = random.randint(0, 1000000) - 2
                    range_end = range_begin + 1

                    children_infection_percentage = random.randint(10, 20)
                    adult_infection_percentage = random.randint(15, 40)
                    senior_infection_percentage = random.randint(35, 60)

                    # loop through the range of citizens
                    for person_index in range(range_begin, range_end + 1):
                        person = (Community.all_citizens[person_index])

                        # print(f"f family id is :{person.family_id}")

                        probability = random.randint(0, 100)
                        person_in_inf_list = False
                        for each_person in inf_list:
                            if each_person.citizen_id == person.citizen_id:
                                person_in_inf_list = True
                                break
                        if person_in_inf_list is False:
                            if person.type == 1:

                                if probability <= children_infection_percentage:
                                    person.is_infected = True
                                    total_covid_cases = total_covid_cases + 1
                                    covid_cases_for_day = covid_cases_for_day + 1
                                    # print(f"Citizen with citizen_id {person.citizen_id} got infected")
                                    inf_list.append(person)
                                    # Covid.infected.append(person)
                            elif person.type == 2:
                                if probability <= adult_infection_percentage:
                                    person.is_infected = True
                                    total_covid_cases = total_covid_cases + 1
                                    covid_cases_for_day = covid_cases_for_day + 1
                                    # if person not in inf_list:
                                    inf_list.append(person)
                                    # Covid.infected.append(person)
                            else:
                                if probability <= senior_infection_percentage:
                                    person.is_infected = True
                                    total_covid_cases = total_covid_cases + 1
                                    covid_cases_for_day = covid_cases_for_day + 1
                                    # if person not in inf_list:
                                    inf_list.append(person)
                                    # Covid.infected.append(person)


                elif Covid.facemask_policy is True and Covid.travel_restriction_enforcement is False:

                    range_begin = random.randint(0, 1000000) - 2
                    range_end = range_begin + 1
                    infection_percentage = random.randint(5, 10)

                    # loop through the range of citizens
                    for person_index in range(range_begin, range_end + 1):
                        person = (Community.all_citizens[person_index])

                        # print(f"f family id is :{person.family_id}")

                        probability = random.randint(0, 100)
                        person_in_inf_list = False
                        for each_person in inf_list:
                            if each_person.citizen_id == person.citizen_id:
                                person_in_inf_list = True
                                break
                        if person_in_inf_list is False:
                            if probability <= infection_percentage:
                                person.is_infected = True
                                total_covid_cases = total_covid_cases + 1
                                covid_cases_for_day = covid_cases_for_day + 1
                                inf_list.append(person)
                                # Covid.infected.append(person)


                elif Covid.facemask_policy is False and Covid.travel_restriction_enforcement is True:

                    # only essential service people gets infected through community
                    range_begin = random.randint(0, 1000000) - 2
                    range_end = range_begin + 1
                    infection_percentage = random.randint(15, 40)

                    # loop through the range of citizens
                    for person_index in range(range_begin, range_end + 1):
                        person = (Community.all_citizens[person_index])

                        # print(f"f family id is :{person.family_id}")

                        probability = random.randint(0, 100)
                        person_in_inf_list = False
                        for each_person in inf_list:
                            if each_person.citizen_id == person.citizen_id:
                                person_in_inf_list = True
                                break
                        if person_in_inf_list is False and person.is_in_essensial_service is True:
                            if probability <= infection_percentage:
                                person.is_infected = True
                                total_covid_cases = total_covid_cases + 1
                                covid_cases_for_day = covid_cases_for_day + 1
                                inf_list.append(person)
                                # Covid.infected.append(person)




                else:

                    # only essential service people gets infected through community and the probability is low
                    # only essential service people gets infected through community
                    range_begin = random.randint(0, 1000000) - 2
                    range_end = range_begin + 1
                    infection_percentage = random.randint(5, 10)

                    # loop through the range of citizens
                    for person_index in range(range_begin, range_end + 1):
                        person = (Community.all_citizens[person_index])

                        # print(f"f family id is :{person.family_id}")

                        probability = random.randint(0, 100)
                        person_in_inf_list = False
                        for each_person in inf_list:
                            if each_person.citizen_id == person.citizen_id:
                                person_in_inf_list = True
                                break
                        if person_in_inf_list is False and person.is_in_essensial_service is True:
                            if probability <= infection_percentage:
                                person.is_infected = True
                                total_covid_cases = total_covid_cases + 1
                                covid_cases_for_day = covid_cases_for_day + 1
                                inf_list.append(person)
                                # Covid.infected.append(person)

        hospitalization_count = 0
        recovered_count = 0
        for each_person in inf_list:
            # print("Each person athule")
            if each_person not in Covid.infected:
                Covid.infected.append(each_person)
        # print(f"Covid Cases for day : {covid_cases_for_day}")
        for each_infected_person in Covid.infected:
            hospitalization_day = random.randint(5, 11)
            if each_infected_person.number_of_days_infected >= hospitalization_day:
                each_infected_person.is_hospitalized = True
                hospitalization_count = hospitalization_count + 1
            each_infected_person.number_of_days_infected = each_infected_person.number_of_days_infected + 1
            if each_infected_person.is_hospitalized:
                each_infected_person.hospitalized_days = each_infected_person.hospitalized_days + 1
            if each_infected_person.hospitalized_days >= 10 and not each_infected_person.is_recovered:
                each_infected_person.is_recovered = True
                recovered_count = recovered_count + 1

        death_count = int(total_covid_cases / 1000)
        today_death_count = death_count - previous_death_count
        previous_death_count = death_count

        today = Day()
        today.day_number = day
        today.infected = covid_cases_for_day
        today.hospitalized = hospitalization_count
        today.recovered = recovered_count
        today.fatalities = today_death_count
        days_list.append(today)

        print(f"Covid positive cases   : {today.infected}")
        print(f"Covid deaths           : {today.fatalities}")
        print(f"Covid hospitalizations : {today.hospitalized}")
        print(f"Covid recovers         : {today.recovered}")
        # print(f"Day {day} after the Outbreak")
        print("Options : ")
        if Covid.facemask_policy is False:
            facemask_policy = str(input("     Do you want to enable facemask policy? (y/n)"))
            if facemask_policy == 'y':
                Covid.facemask_policy = True
        else:
            facemask_policy = str(input("     Do you want to disable facemask policy? (y/n)"))
            if facemask_policy == 'y':
                Covid.facemask_policy = False
        if Covid.travel_restriction_enforcement is False:
            travel_policy = str(input("     Do you want to enable travel restriction policy? (y/n)"))
            if travel_policy == "y":
                Covid.travel_restriction_enforcement = True
        else:
            travel_policy = str(input("     Do you want to disable travel restriction policy? (y/n)"))
            if travel_policy == "y":
                Covid.travel_restriction_enforcement = False

    # for citizen in Community.all_citizens:
    #     if citizen.is_infected:
    # print(f"{citizen.family_id}")

    # print(f"Citizen ge : {Community.all_citizens[citizen_number].is_infected}")
    # print(f"inf list : {len(inf_list)}")
    # print(f"infected : {len(Covid.infected)}")

    # Covid.infected.extend(inf_list)
    # print(f"Full Cases : {len(Covid.infected)}")
    # for member in Covid.infected:
    #     print(f"Family id : {member.family_id}")
    # for citizen in Community.all_citizens:
    #     if(citizen.citizen_id % 100 is 0):
    #         print(f"citizen id : {citizen.citizen_id}")
    draw_charts(days_list)


def main():
    make_families()
    fill_others()
    set_essensial_service_people()
    infect()


if __name__ == '__main__':
    main()
