import time as t
Lv = int(input("레벨은 무엇입니까?: "))
score = int(input("스코어는 무엇입니까?: "))
clear = str(input("클리어 계수는 어떻습니까?: ")).upper()

while True:
    
    # S랭크 기준
    if score >= 9900000:
        grade = 1.05
        k = (Lv * 2 * score / 10000000) * grade
        
        if clear in ["PUC", "PERFECT ULTIMATE CHAIN", "피유씨"]:
            vf = k * 1.1
            print("VF:%.2f" %vf)
            break
        elif clear in ["UC", "ULTIMATE CHAIN", "유씨"]:
            vf = k * 1.05
            print("VF:%.2f" %vf)
            break
        elif clear in ["EX COMPLETE", "HARD CLEAR", "하드클", "EX클"]:
            vf = k * 1.02
            print("VF:%.2f" %vf)
            break
        elif clear in ["COMPLETE", "일반클", "노말클"]:
            vf = k * 1.00
            print("VF:%.2f" %vf)
            break
        elif clear in ["PLAYED", "못깸"]:
            vf = k * 0.5
            print("VF: %.2f" %vf)
            break
    
    # AAA+랭크 기준
    elif score >= 9800000:
        grade = 1.02
        k = (Lv * 2 * score / 10000000) * grade
        
        if clear in ["PUC", "PERFECT ULTIMATE CHAIN", "피유씨"]:
            vf = k * 1.1
            print("VF:%.2f" %vf)
            break
        elif clear in ["UC", "ULTIMATE CHAIN", "유씨"]:
            vf = k * 1.05
            print("VF:%.2f" %vf)
            break
        elif clear in ["EX COMPLETE", "HARD CLEAR", "하드클", "EX클"]:
            vf = k * 1.02
            print("VF:%.2f" %vf)
            break
        elif clear in ["COMPLETE", "일반클", "노말클"]:
            vf = k * 1.00
            print("VF:%.2f" %vf)
            break
        elif clear in ["PLAYED", "못깸"]:
            vf = k * 0.5
            print("VF: %.2f" %vf)
            break
    
    # AAA랭크 기준
    elif score >= 9700000:
        grade = 1.00
        k = (Lv * 2 * score / 10000000) * grade
        
        if clear in ["PUC", "PERFECT ULTIMATE CHAIN", "피유씨"]:
            vf = k * 1.1
            print("VF:%.2f" %vf)
            break
        elif clear in ["UC", "ULTIMATE CHAIN", "유씨"]:
            vf = k * 1.05
            print("VF:%.2f" %vf)
            break
        elif clear in ["EX COMPLETE", "HARD CLEAR", "하드클", "EX클"]:
            vf = k * 1.02
            print("VF:%.2f" %vf)
            break
        elif clear in ["COMPLETE", "일반클", "노말클"]:
            vf = k * 1.00
            print("VF:%.2f" %vf)
            break
        elif clear in ["PLAYED", "못깸"]:
            vf = k * 0.5
            print("VF: %.2f" %vf)
            break
    
    # AA+랭크 기준
    elif score >= 9500000:
        grade = 0.97
        k = (Lv * 2 * score / 10000000) * grade
        
        if clear in ["PUC", "PERFECT ULTIMATE CHAIN", "피유씨"]:
            vf = k * 1.1
            print("VF:%.2f" %vf)
            break
        elif clear in ["UC", "ULTIMATE CHAIN", "유씨"]:
            vf = k * 1.05
            print("VF:%.2f" %vf)
            break
        elif clear in ["EX COMPLETE", "HARD CLEAR", "하드클", "EX클"]:
            vf = k * 1.02
            print("VF:%.2f" %vf)
            break
        elif clear in ["COMPLETE", "일반클", "노말클"]:
            vf = k * 1.00
            print("VF:%.2f" %vf)
            break
        elif clear in ["PLAYED", "못깸"]:
            vf = k * 0.5
            print("VF: %.2f" %vf)
            break
    
    # AA랭크 기준
    elif score >= 9300000:
        grade = 0.94
        k = (Lv * 2 * score / 10000000) * grade
        
        if clear in ["PUC", "PERFECT ULTIMATE CHAIN", "피유씨"]:
            vf = k * 1.1
            print("VF:%.2f" %vf)
            break
        elif clear in ["UC", "ULTIMATE CHAIN", "유씨"]:
            vf = k * 1.05
            print("VF:%.2f" %vf)
            break
        elif clear in ["EX COMPLETE", "HARD CLEAR", "하드클", "EX클"]:
            vf = k * 1.02
            print("VF:%.2f" %vf)
            break
        elif clear in ["COMPLETE", "일반클", "노말클"]:
            vf = k * 1.00
            print("VF:%.2f" %vf)
            break
        elif clear in ["PLAYED", "못깸"]:
            vf = k * 0.5
            print("VF: %.2f" %vf)
            break
    
    # A+랭크 기준
    elif score >= 9000000:
        grade = 0.91
        k = (Lv * 2 * score / 10000000) * grade
        
        if clear in ["PUC", "PERFECT ULTIMATE CHAIN", "피유씨"]:
            vf = k * 1.1
            print("VF:%.2f" %vf)
            break
        elif clear in ["UC", "ULTIMATE CHAIN", "유씨"]:
            vf = k * 1.05
            print("VF:%.2f" %vf)
            break
        elif clear in ["EX COMPLETE", "HARD CLEAR", "하드클", "EX클"]:
            vf = k * 1.02
            print("VF:%.2f" %vf)
            break
        elif clear in ["COMPLETE", "일반클", "노말클"]:
            vf = k * 1.00
            print("VF:%.2f" %vf)
            break
        elif clear in ["PLAYED", "못깸"]:
            vf = k * 0.5
            print("VF: %.2f" %vf)
            break
    
    # A랭크 기준
    elif score >= 8700000:
        grade = 0.88
        k = (Lv * 2 * score / 10000000) * grade
        
        if clear in ["PUC", "PERFECT ULTIMATE CHAIN", "피유씨"]:
            vf = k * 1.1
            print("VF:%.2f" %vf)
            break
        elif clear in ["UC", "ULTIMATE CHAIN", "유씨"]:
            vf = k * 1.05
            print("VF:%.2f" %vf)
            break
        elif clear in ["EX COMPLETE", "HARD CLEAR", "하드클", "EX클"]:
            vf = k * 1.02
            print("VF:%.2f" %vf)
            break
        elif clear in ["COMPLETE", "일반클", "노말클"]:
            vf = k * 1.00
            print("VF:%.2f" %vf)
            break
        elif clear in ["PLAYED", "못깸"]:
            vf = k * 0.5
            print("VF: %.2f" %vf)
            break
    
    # B랭크 기준
    elif score >= 7500000:
        grade = 0.85
        k = (Lv * 2 * score / 10000000) * grade
        
        if clear in ["PUC", "PERFECT ULTIMATE CHAIN", "피유씨"]:
            vf = k * 1.1
            print("VF:%.2f" %vf)
            break
        elif clear in ["UC", "ULTIMATE CHAIN", "유씨"]:
            vf = k * 1.05
            print("VF:%.2f" %vf)
            break
        elif clear in ["EX COMPLETE", "HARD CLEAR", "하드클", "EX클"]:
            vf = k * 1.02
            print("VF:%.2f" %vf)
            break
        elif clear in ["COMPLETE", "일반클", "노말클"]:
            vf = k * 1.00
            print("VF:%.2f" %vf)
            break
        elif clear in ["PLAYED", "못깸"]:
            vf = k * 0.5
            print("VF: %.2f" %vf)
            break
        
    # C랭크 기준
    elif score >= 6500000:
        grade = 0.82
        k = (Lv * 2 * score / 10000000) * grade
        
        if clear in ["PUC", "PERFECT ULTIMATE CHAIN", "피유씨"]:
            vf = k * 1.1
            print("VF:%.2f" %vf)
            break
        elif clear in ["UC", "ULTIMATE CHAIN", "유씨"]:
            vf = k * 1.05
            print("VF:%.2f" %vf)
            break
        elif clear in ["EX COMPLETE", "HARD CLEAR", "하드클", "EX클"]:
            vf = k * 1.02
            print("VF:%.2f" %vf)
            break
        elif clear in ["COMPLETE", "일반클", "노말클"]:
            vf = k * 1.00
            print("VF:%.2f" %vf)
            break
        elif clear in ["PLAYED", "못깸"]:
            vf = k * 0.5
            print("VF: %.2f" %vf)
            break
        
    # D랭크 기준
    else:
        grade = 0.8
        k = (Lv * 2 * score / 10000000) * grade
        
        if clear in ["PUC", "PERFECT ULTIMATE CHAIN", "피유씨"]:
            vf = k * 1.1
            print("VF:%.2f" %vf)
            break
        elif clear in ["UC", "ULTIMATE CHAIN", "유씨"]:
            vf = k * 1.05
            print("VF:%.2f" %vf)
            break
        elif clear in ["EX COMPLETE", "HARD CLEAR", "하드클", "EX클"]:
            vf = k * 1.02
            print("VF:%.2f" %vf)
            break
        elif clear in ["COMPLETE", "일반클", "노말클"]:
            vf = k * 1.00
            print("VF:%.2f" %vf)
            break
        elif clear in ["PLAYED", "못깸"]:
            vf = k * 0.5
            print("VF: %.2f" %vf)
            break

t.sleep(15)   
    
    
    
    