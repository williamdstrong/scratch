raw_text="            String firstName,            String lastName,            String emailAddress,            String username,            boolean male,            int birthMonth,            int birthDay,            int birthYear,            String password,            String confirmPassword,            String homePhone,            String mobilePhone,            String address,            String address2,            String city,            String state,            String zip,            String securityQuestion,            String securityQuestionAnswer"

l = raw_text.split("          ")

ln = []
for i in l:
    ln.append(i.strip())
print(ln)

def make_function(s):
    s = s.replace(",", "")
    
    list = s.split(" ")
    print(list)
    
    return "{0} {1} = ParamUtil.get{0}(request, \"{1}\");".format(list[0], list[1]) 

def make_function_list(text_list):
    print(text_list)
    function_list = []
    for text in text_list:
        if text != "":
            function_list.append(make_function(text))

    return function_list

for i in make_function_list(ln):
    print(i)
