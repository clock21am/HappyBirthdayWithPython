import sys
sys.path.append("/some/path") 
import facebook
import json
import requests

tokeen='EAACEdEose0cBALxAhYZADlZCRs9sriQVmaFZAeTeASY5wSzUTJluvQsKN7Ykwj05M1lRT4cGTZBLYMh2o7am0W8ZAxZBTlF9ibjo4xUi8Mp3f5A7MDyoCFkwxWE8pbQGfMOlrX28Cmqaeqevll0ZCodk0Mnu620OIkshdwfDaNeAQZDZD'
  
def main():
    graph = facebook.GraphAPI(access_token=tokeen,version='2.2')
    post = graph.get_object(id="me")
    #graph.put_object(parent_object='me', connection_name='feed',message='Have a good day')
    feeds = graph.get_connections(post["id"],"feed")
    result = json.dumps(feeds)
    print(result)
    for feeds in feeds["data"]:
       try: 
           if feeds["created_time"] > "2015-02-08T06:43:34+0000":
               graph.put_object(feeds["id"],"likes")
               graph.put_object(feeds["id"],connection_name="comments",message="Thank you sooo much :)")
       except:
           print("nothing")
     
    

if __name__ == '__main__':
    main()










