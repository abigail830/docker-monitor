from dockermon.ContainerInfoCollector import ContainerInfoCollector

if __name__ == '__main__':

    collect = ContainerInfoCollector()
    print("Going to access docker ...")

    collect.collect_info_list()
