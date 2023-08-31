from result_output import *
import sys
import json
import importlib.util
import urllib.request
from googleapiclient import discovery
from google.oauth2 import service_account
from pprint import pprint
from google.cloud import storage
from google.cloud import container_v1
from googleapiclient import discovery
from google.cloud.container_v1 import ClusterManagerClient
from kubernetes import client
import google.auth.transport.requests
import urllib3

class Activity():

    def testcase_check_GKE_Cluster_name(self,test_object,credentials,project_id):
        testcase_description="Check GKE Cluster name"
        expected_result='my-app-cluster'
        try:
            is_present = False
            actual = 'GKE Cluster name is not '+ expected_result
            try:
                service = discovery.build('container', 'v1', credentials=credentials)
                request = service.projects().zones().clusters().list(projectId=project_id, zone='-')
                response = request.execute()  
                if 'clusters' in response:
                    for cluster in response['clusters']:
                        if cluster['name'] == expected_result:
                            is_present = True
                            actual=expected_result
                            break
                        else:
                            actual = cluster['name']
                            pass
            except Exception as e:
                is_present = False
            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"No Comment"," Congrats! You have done it right!") 
            else:
                test_object.update_result(0,expected_result,actual,"Check GKE Cluster","https://cloud.google.com/kubernetes-engine/docs/")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_GKE_Cluster_name"]=str(e)                

    def testcase_check_GKE_Cluster_Region(self,test_object,credentials,project_id):
        testcase_description="Check GKE Cluster Region"
        expected_result='us-central1'
        try:
            is_present = False
            actual = 'GKE Cluster Region is not '+ expected_result
            try:
                service = discovery.build('container', 'v1', credentials=credentials)
                request = service.projects().zones().clusters().list(projectId=project_id, zone='-')
                response = request.execute()  
                if 'clusters' in response:
                    for cluster in response['clusters']:
                        if expected_result in cluster['zone'] :
                            is_present = True
                            actual=expected_result
                            break
                        else:
                            actual = cluster['zone']
                            pass
            except Exception as e:
                is_present = False
            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"No Comment"," Congrats! You have done it right!") 
            else:
                test_object.update_result(0,expected_result,actual,"Check GKE Cluster Region","https://cloud.google.com/kubernetes-engine/docs/")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_GKE_Cluster_name"]=str(e)                

    def testcase_check_GKE_Pool_name(self,test_object,credentials,project_id):
        testcase_description="Check GKE Pool name"
        expected_result='my-app-pool'
        try:
            is_present = False
            actual = 'GKE Pool name is not '+ expected_result
            try:
                service = discovery.build('container', 'v1', credentials=credentials)
                request = service.projects().zones().clusters().list(projectId=project_id, zone='-')
                response = request.execute()  
                if 'clusters' in response:
                    for cluster in response['clusters']:
                        if expected_result in [d.get('name', None) for d in cluster['nodePools']] :
                            is_present = True
                            actual=expected_result
                            break
                        else:
                            actual = [d.get('name', None) for d in cluster['nodePools']]
                            pass
            except Exception as e:
                is_present = False
            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"No Comment"," Congrats! You have done it right!") 
            else:
                test_object.update_result(0,expected_result,actual,"Check GKE Cluster Pool","https://cloud.google.com/kubernetes-engine/docs/")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_GKE_Cluster_name"]=str(e)                

    def testcase_check_Node_numbers(self,test_object,credentials,project_id):
        testcase_description="Check GKE Cluster Nodes Count"
        expected_result=2
        try:
            is_present = False
            actual = 'GKE Cluster nodes is not '+ str(expected_result)
            try:
                service = discovery.build('container', 'v1', credentials=credentials)
                request = service.projects().zones().clusters().list(projectId=project_id, zone='-')
                response = request.execute()  
                if 'clusters' in response:
                    for cluster in response['clusters']:
                        if cluster['currentNodeCount'] == expected_result:
                            is_present = True
                            actual=expected_result
                            break
                        else:
                            actual=cluster['currentNodeCount']
                            pass
            except Exception as e:
                is_present = False
            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"No Comment"," Congrats! You have done it right!") 
            else:
                test_object.update_result(0,expected_result,actual,"Check GKE Node","https://cloud.google.com/kubernetes-engine/docs")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_Node_numbers"]=str(e)  
            
    def testcase_check_GKE_Network_name(self,test_object,credentials,project_id):
        testcase_description="Check GKE Network name"
        expected_result='developer-vpc'
        try:
            is_present = False
            actual = 'GKE Cluster Netowrk name is not '+ expected_result
            try:
                service = discovery.build('container', 'v1', credentials=credentials)
                request = service.projects().zones().clusters().list(projectId=project_id, zone='-')
                response = request.execute()  
                if 'clusters' in response:
                    for cluster in response['clusters']:
                        if cluster['network'] == expected_result:
                            is_present = True
                            actual=expected_result
                            break
                        else:
                            actual = cluster['network']
                            pass
            except Exception as e:
                is_present = False
            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"No Comment"," Congrats! You have done it right!") 
            else:
                test_object.update_result(0,expected_result,actual,"Check GKE Cluster Network","https://cloud.google.com/kubernetes-engine/docs/")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_GKE_Cluster_name"]=str(e)                

    def testcase_check_GKE_SubNetwork_name(self,test_object,credentials,project_id):
        testcase_description="Check GKE Subnet name"
        expected_result='private-dev-subnet'
        try:
            is_present = False
            actual = 'GKE SubNet name is not '+ expected_result
            try:
                service = discovery.build('container', 'v1', credentials=credentials)
                request = service.projects().zones().clusters().list(projectId=project_id, zone='-')
                response = request.execute()  
                if 'clusters' in response:
                    for cluster in response['clusters']:
                        if cluster['subnetwork'] == expected_result:
                            is_present = True
                            actual=expected_result
                            break
                        else:
                            actual = cluster['subnetwork']
                            pass
            except Exception as e:
                is_present = False
            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"No Comment"," Congrats! You have done it right!") 
            else:
                test_object.update_result(0,expected_result,actual,"Check GKE Subnet","https://cloud.google.com/kubernetes-engine/docs/")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_GKE_Cluster_name"]=str(e)                
    
def start_tests(credentials, project_id, args):

    if "result_output" not in sys.modules:
        importlib.import_module("result_output")
    else:
        importlib.reload(sys.modules[ "result_output"])
    
    test_object=ResultOutput(args,Activity)
    challenge_test=Activity()

    challenge_test.testcase_check_GKE_Cluster_name(test_object,credentials,project_id)
    challenge_test.testcase_check_GKE_Cluster_Region(test_object,credentials,project_id)
    challenge_test.testcase_check_GKE_Pool_name(test_object,credentials,project_id)
    challenge_test.testcase_check_Node_numbers(test_object,credentials,project_id)
    challenge_test.testcase_check_GKE_Network_name(test_object,credentials,project_id)
    challenge_test.testcase_check_GKE_SubNetwork_name(test_object,credentials,project_id)

    json.dumps(test_object.result_final(),indent=4)
    return test_object.result_final()
