from ..models import UserIpfsGateway
from helpers import IpfsHelper

class UserIpfsGatewayService:
    
    @staticmethod
    def saveUserIpfsRecord(walletAddress, cid):
        userIpfsGateway = UserIpfsGateway(walletAddress = walletAddress, cid = cid)
        userIpfsGateway.save()
        return True
    
    def deleteUserIpfsRecord(walletAddress: str):
        return UserIpfsGateway.objects.filter(walletAddress=walletAddress).delete()
        
    def getUserIpfsData(walletAddress):
        return IpfsHelper.fetchData(UserIpfsGateway.objects.get(walletAddress = walletAddress).cid)
    
    def getAllUserIpfsData():
        return [IpfsHelper.fetchData(userIpfsRecord.cid) for userIpfsRecord in UserIpfsGateway.objects.all()]

        