# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20816 정소여
# 프로젝트 주제: 신약 물질 후보 개발
compounds = [
    ["Compound_A", 350.4, 3.2, 3],  
    ["Compound_B",523.1, 4.5, 2],  
    ["Compound_C", 410.2, 7.8, 1],  
    ["Compound_D", 150.8, 1.2, 2],  
    ["Compound_E", 480.0, 0.5, 6]   
]
def check_lipinski(compound):
    name = compound[0]
    mw = compound[1]      
    logp = compound[2]    
    donor = compound[3]   
    
    if mw <= 500 and logp <= 5 and _donor<=5:
        return "SUCCESS"
    else:
        return "FAIL" 
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