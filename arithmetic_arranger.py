question = input("Enter: ")
question=question.split(',')

def calculate(question,diplay_anwers=None):
    if len(question)>5:
        return ('Error: Too many problems.')
    first_operand = list()
    second_operand = list()
    answers = list()
    operators =list()
    for i in question:
        nums=[]
        if (('+' in i)or ('-' in i)):
            for symbols in ['+','-']:
                if symbols in i:
                    operator = symbols
                    operators.append(operator)
                    nums=i.split(operator)
                    if nums[0].isdigit() and nums[1].isdigit():
                        if len(nums[0])>4 or len(nums[1])>4:
                            return "Error: Numbers cannot be more than four digits."
                        else:
                            first_operand.append(nums[0])
                            second_operand.append(nums[1])
                    else:
                        return ('Error: Numbers must only contain digits.')

                else:
                    continue
                if diplay_anwers == True:
                    if operator == '+':
                        answer = str(int(nums[0])+int(nums[1]))
                        answers.append(answer)
                    else:
                        answer = str(int(nums[0]) - int(nums[1]))
                        answers.append(answer)

        else:
            return ("Error: Operator must be '+' or '-'")


        first_row = list()
        second_row = list()
        third_row = list()
        fourth_row = list()

        for i in range(len(first_operand)):
                if len(first_operand[i])>=len(second_operand[i]):
                    first_row.append('  '+first_operand[i])
                else:
                    space=(len(second_operand[i])-len(first_operand[i]))
                    first_row.append("  "+" "*space+first_operand[i])
                third_row.append("-" * (max(len(first_operand[i]), len(second_operand[i]))+2))
        for i in range(len(second_operand)):
                if len(second_operand[i])<len(first_operand[i]):
                    space = (len(first_operand[i]) - len(second_operand[i]))
                    second_row.append(operators[i]+" "+" "*space+second_operand[i])
                else:
                    second_row.append(operators[i]+" "+second_operand[i])
        for i in range(len(answers)):
            if len(answers[i])>max(len(first_operand[i]),len(second_operand[i])):
                fourth_row.append(' '+answers[i])
            else:
                fourth_row.append('  '+answers[i])

        final = '    '.join(first_row)+'\n'+'    '.join(second_row)+'\n'+'    '.join(third_row)+'\n'+'    '.join(fourth_row)

    return final

print(calculate(question,True))
