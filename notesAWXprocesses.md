# thoughts on automating a two step process (TEAM A / TEAM B) with 3 playbooks
# email rzfeeser@alta3.com for help on evolving this model


# Playbook 1
1) Team A sends to Team B
    - with "service now"
    - REST API calls & creating
    - uri module to role dev to allow users to start a change process (ansible to Service now API)

# Playbook 2
2) Team B (to respond to team A, has set up AWX to respond to incoming "service now" events
    - up receiving request
    - data is cut out of incoming request
    ## 
    - data is added to end of config
    
    tasks:
    - template module
        - ### comment
        - ### config to be added
        
    - archive
        - create a copy of file about to be changed
        - MAKE SURE YOU DONT THROW THE FLAG TO ERASE THE FILE AFTER IT IS ARCHIVED
        - this will auto timestamp it as well
    
    - block-in-file
        - EOF
        - targeting the cfg file that needs bounced
        - handler maybe creates a flag file... maybe write the name of the services to be restarted into a common file


    handler:
    - line-in-file
        - put a line into the bottom of the file for service to be restarted
        - REMEMBER to check that the service isn't ALREADY in the file

    

# Playbook 3 (scheduled)
# https://docs.ansible.com/ansible-tower/latest/html/userguide/scheduling.html
    ## AWX can schedule jobs to run at certain times
    vars:
        - lookup(on file containing services to be restarted)
    
    restart
        - looping across services in our "flag file"
