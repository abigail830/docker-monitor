import requests_unixsocket
import json
from dockermon.ContainerInfo import ContainerInfo
from util.util import Utils
u = Utils()


class ContainerInfoCollector:

    def __init__(self):
        self.base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
        self.url = "/containers/json"
        self.session = requests_unixsocket.Session()
        try:
            self.resp = self.session.get( self.base + self.url)
        except Exception as ex:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def collect_info_list(self):
        resp = self.resp
        u.check_resp(resp.status_code, self.url)

        info_list=[]
        for item in resp.json():
            item_info = ContainerInfo(item)
            # print("{}".format(item_info.__str__()))
            info_list.append(item_info)

        json_result = json.dumps(info_list.__dict__)
        print("{}".format(json_result))
        return json_result
