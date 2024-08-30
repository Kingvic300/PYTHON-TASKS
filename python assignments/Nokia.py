def runMatch():
    menu_option = """
        1 -> PhoneBook
	2 -> Messages
	3 -> Chat
	4 -> Call Register
	5 ->Tones
	6 ->Settings
	7 -> Call Divert
	8 -> Games
	9 -> Calculator
	10 -> Reminders
	11 -> Clock
	12 -> Profiles
	13 -> SIM Services

    """
    print(menu_option)
    option = int(input("Enter A Number:"))

    match option:
        case 1:
            print("phonebook")
            def phonebook():
                menu = """
                1. Search
                2.Service Nos
                3. Add Name
                4. Erase
                5.Edit
                6.Assign Tone
                7. Send b'card
                8.Options
                9. Speed DIals
                10. Voice Tags
                11. Go Back
                """
                print(menu)
                input = int(input("Choose: "))
                match input:
                    case 1: print("Search")
                    case 2: print("Service Nos")
                    case 3: print("Add Name")
                    case 4: print("Erase")
                    case 5: print("Edit")
                    case 6: print("Assign Tone")
                    case 7: print("Send b'card")
                    case 8:
                        print("Options")
                        def option():
                            option = """
                            1. Types of Views
                            2. Memory Status
                            0. Back
                            """
                            print(option)
                            input = int(input("Choose: "))
                            match input:
                                case 1: print("Types Of Views")
                                case 2: print("Memory Status")
                                case 0:
                                    print("back")
                                    phonebook()
                                
                                
                        option()
                    case 9: print("Speed Dials")
                    case 10: print("Voice Tags")
                    case 11:
                        print("Go Back")
                        runMatch();
                        
                    
            phonebook()
        case 2:
            print("Messages")
            def messages():
                Messages = """
                1. Write Messages
                2. Inbox
                3. Outbox
                4.Picture
                5.Template
                6. Smileys
                7. Message Settings
                8. Info Service
                9. Voice Mailbox Number
                10. Service Command editor
                0. Go Back
                """
                print(Messages)
                inbox = int(input("Choose: "))
                match inbox:
                    case 1:print("Write Messages")
                    case 2:print("Inbox")
                    case 3:print("Outbox")
                    case 4:print("Pictures")
                    case 5:print("Template")
                    case 6:print("Smileys")
                    case 7:
                        print("Message Settings")
                        def message_settings():
                            Message_settings = """
                            1. Set
                            2.Common
                            0.Go BAck
                            """
                            print(option)
                            option = int(input("Choose: "))
                            match option:
                                case 1:
                                    print("Set")
                                    def set():
                                        sets = """
                                        1. Message centre number
                                        2. Messages sent as
                                        3. Message validity
                                        0. Back
                                        """
                                        print(sets)
                                        option = int(input("Choose: "))
                                        if option == 1: print("Message centre number")
                                        elif option == 2: print("Messages sent as")
                                        elif option == 3: print("Message validity")
                                        elif option == 0: print("Back")
                                        Message_settings()
                                        
                                    set()
                                case 2:
                                    print("Common")
                                    def common():
                                        commons = """
                                        1. Delivery reports
                                        2. Reply via same centre
                                        3. Character support
                                        0. Back
                                        """
                                        print(commons)
                                        common = int(input("Choose: "))
                                        if common == 1: print("Delivery reports")
                                        elif common == 2: print("Reply via same centre")
                                        elif common == 3: print("Character support")
                                        elif common == 0: print("Back")
                                        Message_settings()
                                    common()
                                case 0:
                                    print("Go back")
                                    messages()
        
                        Message_settings()
                    case 8: print("Info Service")
                    case 9: print("Voice mailbox")
                    case 10: print("service command ....")
                    case 0:
                        print("Go Back")
                        runMatch()
            messages()
        case 3: print("Chat")
        case 4:
            print("Call Register")
            call_register = """
            1. Missed calls
            2. Received calls
            3. Dialled numbers
            4. Erase recent call lists
            5. Show call duration
            6. Show call costs
            7. Call cost settings
            8. Prepaid credit
            """
            print(call_register)
            register = int(input("Choose: "))
            match register:
                case 1: print("Missed calls")
                case 2: print("Received calls")
                case 3: print("Dialled numbers")
                case 4: print("Erase recent call lists")
                case 5:
                    print("Show call duration")
                    def call_duration():
                        duration = """
                        1. Last Call Duration
                        2. All calls’ duration
                        3. Received calls’ duration
                        4. Dialled calls’ duration
                        5. Clear timers
                        """
                        print(duration)
                        duration = int(input("Choose: "))
                        if duration == 1: print("Last Call Duration")
                        elif duration == 2: print("All calls’ duration")
                        elif duration == 3: print("Received calls’ duration")
                        elif duration == 4: print("Dialled calls’ duration")
                        else : print("Clear timers")
                    call_duration()
                case 6:
                    print("Show call costs")
                    def call_costs():
                        call_cost = """
                        1.Last call cost
                        2. All calls’ cost
                        3.Clear counters
                        """
                        print(call_cost)
                        cost = int(input("Choose: "))
                        if cost == 1: print("Last call cost")
                        elif cost == 2: print("All calls’ cost")
                        else: print("Clear Counter")
                    call_costs()
                case 7:
                    print("Call cost")
                    def call_costs():
                        cost_settings = """
                        1. Call cost limit
                        2. Show costs in
                        """
                        print(cost_settings)
                        call_cost = int(input("Choose: "))
                        if call_cost == 1: print("Call cost limit")
                        else: print("Show costs in")
                    call_costs()
                case 8: print("Prepaid credit")
        case 5:
            print("Tone")
            tone = """
            1. Ringing tone
            2. Ringing volume
            3. Incoming call alert
            4. Composer
            5. Message alert tone
            6. Keypad tones
            7. Warning and game tones
            8. Vibrating alert
            9. Screen saver
            """
            print(tones)
            tones = int(input("Choose: "))
            match tones:
                case 1:print("Ringing tone")
                case 2:print("Ringing volume")
                case 3:print("Incoming call alert")
                case 4:print("Composer")
                case 5:print("Message alert tone")
                case 6:print("Keypad tones")
                case 7:print("Warning and game tones")
                case 8:print("Vibrating alert")
                case 9:print("Screen saver")

        case 6:
            print("Settings")
            def settings():
                setting = """
                1. Call settings
                2.Phone settings
                3. Security settings
                4. Restore factory settings
                """
                print(setting)
                setting =  int(input("Choose: "))
                match setting:
                    case 1:
                        print("Call Settings")
                        def calls():
                            calls = """
                            1. Automatic redial
                            2. Speed dialling
                            3. Call waiting options
                            4. Own number sending
                            5. Phone line in use
                            6. Automatic answer
                            """
                            print(call)
                            call = int(input("Enter: "))
                            match call:
                                case 1: print("Auto Redial")
                                case 2: print("Speed dialling")
                                case 3: print("Call waiting options")
                                case 4: print("Own number sending")
                                case 5: print("Phone line in use")
                                case 6: print("Automatic answer")
                        call_settings()
                    case 2:
                        print("Phone Settings")
                        def phone_settings():
                            phone = """
                            1. Language
                            2. Cell info display
                            3. Welcome note
                            4. Network selection
                            5. Lights 
                            6. Confirm SIM service actions
                            """
                            print(phone)
                            phone = int(input("Enter: "))
                            match phone:
                                case 1: print("Language")
                                case 2: print("Cell info display")
                                case 3: print("Welcome note")
                                case 4: print("Network selection")
                                case 5: print("Lights ")
                                case 6: print("Confirm SIM service actions")
                        phone_settings()
                    case 3:
                        print("Security Settings")
                        def securitys():
                            securitys = """
                            1. PIN code request
                            2. Call barring service
                            3. Fixed dialling
                            4. Closed user group
                            5. Phone security
                            6. Change access codes
                            """
                            print(security_seetings_menu)
                            securities = int(input("Enter: "))
                            match securities:
                                case 1: print("PIN code request")
                                case 2: print("Call barring service")
                                case 3: print("Fixed dialling")
                                case 4: print("Closed user group")
                                case 5: print("Phone security")
                                case 6: print("Change access codes")
                        security_settings()
                    case 4: print("Restore Factory code")
            settings()
        case 7: print("Call Divert")
        case 8: print("Games")
        case 9: print("Calculator")
        case 10: print("Reminders")
        case 11:
            print("Clock")
            def clock():
                clocks = """
                1. Alarm clock
                2. Clock settings
                3. Date setting
                4. Stopwatch
                5. Countdown timer
                6. Auto update of date and time
                """
                print(clocks)
                input = int(input("Choose: "))
                match input:
                    case 1: print("Alarm clock")
                    case 2: print("Clock settings")
                    case 3: print("Date setting")
                    case 4: print("Stopwatch")
                    case 5: print("Countdown timer")
                    case 6: print("Auto update of date and time")
            clock()
        case 12: print("Profiles")
        case 13: print("SIM Services")
                    
runMatch()