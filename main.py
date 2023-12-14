import cv2
import pandas as pd

# read csv file to a list of dictionaries
data = pd.read_csv('D_20220220_1_1620_1650.csv')
# Convert the DataFrame to a Dictionary
data_dict = data.to_dict(orient='records')
#converts data frame rows into list of dictionaries where each row is a seperate dictionary
#print(data_dict)
#Tests to make sure data seperated in dictionary as a list
#prints list of dictionaries, only printing blue team list and not white team too
for item in data_dict:
    print(item)
#was used to create item list to be used in below

# Open the video capture object
video_file_path = 'USE.mp4'
cap = cv2.VideoCapture(video_file_path)

# Check if the video capture object is successfully opened
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Iterate through frames
while True:
    # Read a frame from the video source
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Error: Could not read frame or end of video.")
        break
    for object_info in data_dict:
        #iterates through each instance of the list of dictionaries and then takes the cooresponding data that matches with the index in the dictionary
        bb_left = object_info['0.1']#seen when printing out list of items, each list has a 0,0.1,0.2,0.3, therfore seperating the data
        #instead of being one list from 0 to 0.43, seperated by attribute for each given frame
        bb_top = object_info['0.2']
        bb_width = object_info['0.3']
        bb_height = object_info['0']

        print(f"Object: Bounding Box: ({bb_left}, {bb_top}, {bb_width}, {bb_height})")
        #Each bounding box is recognized and listed as its own object for each player over time

        color = (255, 0, 0)  # blue for team 1 in BGR format
        #thickness = 2
        #cv2.rectangle(frame, (int(bb_left), int(bb_top)), (int(bb_left + bb_width), int(bb_top + bb_height)), color, thickness)
        #What I would do to pass each of these box objects found onto the video frame by frame for the white team during the frames of the video given
    """for ball in data_dict:
        bb_left = ball['BALL.1']  # seen when printing out list of items, each list has a 0,0.1,0.2,0.3, therfore seperating the data
        # instead of being one list from 0 to 0.43, seperated by attribute for each given frame
        bb_top = ball['BALL.2']
        bb_width = ball['BALL.3']
        bb_height = ball['BALL']
        thickness = 2
        color = (0, 0, 255)
        cv2.rectangle(frame, (bb_left, bb_top), ((bb_left + bb_width), (bb_top + bb_height)), color, thickness)#Displays ball


    def are_touching(bb1, bb2, touch_threshold=2):
        x1, y1, w1, h1 = bb1 #x,y,w,h are same as bb_left,bb_top... and bb1 is the first bounding box of the object, specifically the soccer ball
        x2, y2, w2, h2 = bb2 #bbw is the object of the player

        # Calculate center coordinates
        cx1, cy1 = x1 + w1 // 2, y1 + h1 // 2 #avg of the x and width and y and height
        cx2, cy2 = x2 + w2 // 2, y2 + h2 // 2#same as above

        # Calculate distance between centers because if within threshold, then the objects are considered touching and now can see if pass
        distance = ((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2) ** 0.5

        # Check if distance is less than the touch threshold
        if (distance < touch_threshold == True):
            cv2.rectangle(frame, (bb_left, bb_top), ((bb_left + bb_width), (bb_top + bb_height)), (0,255,0), 2)
        elif(distance > touch_threshold):

    #After having the objects be known as touching, I will then go frame by frame and see if the team first in contact with the ball
    #is then tracked to see when the ball breaks through that threshold and is not in contact anymore, if not in contact, go frame by frame
    # until the ball is in contact with another object, and see if it is the same team again or the other team.
    #if same team, all borders light up green for a frame and then go back to original colors
    #if goes to other team then color border lights up red indicating a bad pass


"""
    # Display the frame with bounding boxes
    cv2.imshow('Player Tracking', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close OpenCV windows
cv2.destroyAllWindows()