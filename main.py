
compounds = [
    ["Compound_A", 850.4, 3.2, 3],  
    ["Compound_B", 923.1, 4.5, 2],  
    ["Compound_C", 710.2, 7.8, 1],  
    ["Compound_D", 150.8, 8.2, 2],  
    ["Compound_E", 480.0, 0.5, 8소여]   
]


def check_lipinski(compound):
    name = compound[0]
    mw = compound[1]      
    logp = compound[2]    
    donor = compound[3]   
    
    if mw <= 500 and logp <= 5 and donor <= 5:
        return "SUCCESS"
    else:
        return "FAIL" 


def add_new_compound(data_list):
    print("=========================================")
    print("    후보 물질을 이름, 분자량, 지용성, 수소 주개 순으로 입력하시오   ")
    print("=========================================")
    
   
    name = input( )
    mw = float(input( ))
    logp = float(input( ))
    donor = int(input( ))
    
    
    new_item = [name, mw, logp, donor]
    
  
    data_list.append(new_item)
    print(f"{name} 물질이 성공적으로 리스트에 등록되었습니다!")


def filter_safe_compounds(data_list):
    print("=== 리핀스키 법칙 통과 물질 목록 ===")
    pass_count = 0
    for compound in data_list:
        name = compound[0]
        
        if check_lipinski(compound) == "SUCCESS":
            print(f"- {name}: 분자량 {compound[1]}, 지용성 {compound[2]}, 도너 {compound[3]}")
            pass_count = pass_count + 1 

    if pass_count == 0:
        print("모든 후보 물질이 탈락했습니다.")


if __name__ == "__main__":
    print("=========================================")
    print("   🧬 리핀스키 법칙 신약 후보물질 판별기   ")
    print("=========================================")
    
    
    add_new_compound(compounds)
    
    
    filter_safe_compounds(compounds)
    
    print("=========================================")
    print("프로그램이 성공적으로 종료되었습니다.")