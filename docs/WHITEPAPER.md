# $OTT Whitepaper

### 넘어져도 다시 일어나는 코인 🎎

**Version:** 2.0  
**Date:** February 2026  
**Chain:** Solana  
**Standard:** SPL Token-2022  

> *"Fall Seven Times, Stand Up Eight."* — 七転八起 (칠전팔기)

---

## ⚠️ 면책 조항 (Disclaimer)

**본 백서를 읽기 전, 아래 사항을 반드시 숙지하시기 바랍니다.**

$OTT는 **밈코인**입니다. 본 문서는 $OTT 프로젝트의 비전, 기술 구조, 로드맵을 설명하기 위한 참고 자료이며, **투자 조언, 투자 권유, 또는 수익 보장을 위한 문서가 아닙니다.**

### 투자자 유의사항

1. **원금 손실 위험:** 암호화폐 투자는 원금의 전부 또는 일부를 잃을 수 있습니다. 밈코인은 특히 극단적인 가격 변동성을 가지며, 가치가 0에 수렴할 가능성이 있습니다.

2. **수익 비보장:** $OTT 팀은 토큰의 가격 상승, 유동성 유지, 거래소 상장, 또는 어떠한 형태의 금전적 수익도 보장하지 않습니다.

3. **자기 책임 원칙:** $OTT 토큰의 구매, 보유, 거래, NFT 수령 등 모든 활동은 전적으로 **개인의 판단과 책임** 하에 이루어져야 합니다.

4. **감당 가능한 금액만 사용하십시오:** 잃어도 생활에 지장이 없는 금액만 투자하시기 바랍니다.

5. **독립적 조사 필수 (DYOR):** 투자 전 반드시 독자적인 리서치를 수행하십시오. 본 문서의 정보만으로 투자 결정을 내리지 마십시오.

6. **규제 불확실성:** 암호화폐에 대한 각국의 법률 및 규제는 수시로 변경될 수 있으며, 이는 $OTT의 거래, 보유, 세금에 영향을 줄 수 있습니다.

7. **과거 실적 ≠ 미래 수익:** 다른 프로젝트의 성과가 $OTT의 미래를 보장하지 않습니다.

8. **NFT 에어드롭 과세 가능성:** 일부 국가에서는 NFT 에어드롭 수령이 과세 대상이 될 수 있습니다. 해당 국가의 세법을 확인하시기 바랍니다.

### 법적 고지

- 본 백서는 증권법상 유가증권의 공모 또는 매출을 위한 투자설명서(Prospectus)가 아닙니다.
- $OTT 토큰은 증권, 지분, 채권, 또는 금융상품이 아닙니다.
- $OTT 토큰 보유가 프로젝트의 소유권, 수익 배분권, 의결권을 부여하지 않습니다. (단, Mythic NFT 보유자의 제한적 거버넌스 투표권은 별도 규정에 따릅니다.)
- 프로젝트 팀은 시장 상황, 기술적 한계, 규제 변화 등에 따라 본 백서의 내용을 사전 고지 없이 변경할 수 있습니다.

> **$OTT를 구매하는 것은 위 모든 사항을 이해하고 동의한 것으로 간주합니다.**

---

## 목차 (Table of Contents)

1. [Executive Summary](#1-executive-summary)
2. [프로젝트 배경 및 비전](#2-프로젝트-배경-및-비전)
3. [토큰 이코노미 (Tokenomics)](#3-토큰-이코노미-tokenomics)
4. [NFT 에어드롭 시스템](#4-nft-에어드롭-시스템)
5. [기술 아키텍처](#5-기술-아키텍처)
6. [스마트 컨트랙트 및 온체인 구조](#6-스마트-컨트랙트-및-온체인-구조)
7. [웹사이트 및 프론트엔드](#7-웹사이트-및-프론트엔드)
8. [커뮤니티 전략](#8-커뮤니티-전략)
9. [로드맵](#9-로드맵)
10. [비용 구조 및 운영 투명성](#10-비용-구조-및-운영-투명성)
11. [리스크 분석](#11-리스크-분석)
12. [기술 스택 총정리](#12-기술-스택-총정리)
13. [팀](#13-팀)
14. [부록](#14-부록)

---

## 1. Executive Summary

**$OTT**는 솔라나(Solana) 블록체인 위에 구축된 **감성 유틸리티 밈코인**입니다.

오뚜기(不倒翁) — 쓰러뜨려도 다시 일어나는 인형. 크립토 시장에서 하락을 겪어도 다시 일어나는 홀더들, 인생에서 넘어져도 다시 일어나는 모든 사람들을 응원하는 프로젝트입니다.

### 핵심 요약

| 항목 | 내용 |
|------|------|
| **토큰명 / 티커** | OTT / **$OTT** |
| **체인** | Solana (SPL Token-2022) |
| **총 발행량** | 2,430,000,000,000 (2조 4,300억) |
| **소수점** | 6자리 |
| **발행 방식** | Pump.fun Fair Launch → Raydium 자동 상장 |
| **핵심 유틸리티** | 보유자 자동 응원 NFT 에어드롭 |
| **NFT 기술** | Compressed NFT (cNFT) — Metaplex Bubblegum |
| **NFT 등급** | 5단계 (Common → Rare → Epic → Legendary → Mythic) |
| **NFT 한정** | Legendary 40개, Mythic 3개 |
| **최소 보유량** | 10,000 $OTT (에어드롭 수령 자격) |
| **프리세일 / 프리마이닝** | **없음** — 100% 공정 발행 |

> **$OTT를 보유하면, 당신의 지갑에 응원 메시지가 담긴 NFT가 자동으로 도착합니다.**

---

## 2. 프로젝트 배경 및 비전

### 2.1 왜 오뚜기인가?

오뚜기는 동양 문화권에서 수백 년 동안 사랑받아온 상징입니다.

- 🇰🇷 **한국** — 오뚜기 (불도옹)
- 🇯🇵 **일본** — 다루마 (達磨)
- 🇨🇳 **중국** — 不倒翁 (부도옹)

모두 같은 메시지를 전합니다:

> **"넘어져도 괜찮아, 다시 일어나면 돼."**

크립토 시장은 변동성의 세계입니다. -50%, -90% 하락은 일상이고, 많은 사람들이 좌절합니다. $OTT는 이 시장에서 **정서적 가치**를 제공하는 프로젝트입니다.

### 2.2 우리가 믿는 것

- **모든 사람은 응원받을 자격이 있다** — 포트폴리오가 빨간색이든, 인생이 힘들든
- **커뮤니티는 기술보다 강하다** — 사람들이 모이면 무엇이든 가능하다
- **밈은 문화다** — 밈코인은 단순 투기가 아니라 커뮤니티 문화의 표현이다
- **오뚜기처럼, 다시** 🎎

### 2.3 감성 유틸리티 (Emotional Utility)

$OTT의 유틸리티는 DeFi 수익률이나 거버넌스 투표가 아닙니다.

**당신이 힘들 때, 지갑에 도착하는 따뜻한 메시지 한 마디.**

시장이 폭락한 날, 지갑을 열었을 때 "넘어져도 괜찮아, 다시 일어나면 돼 🎎"라는 메시지가 담긴 NFT를 발견하는 것. 그것이 $OTT가 제공하는 가치입니다.

### 2.4 슬로건

| 번호 | 슬로건 |
|------|--------|
| 1 | **"Fall Seven Times, Stand Up Eight"** (七転八起) |
| 2 | **"넘어져도 괜찮아, 다시 일어나면 돼"** |
| 3 | **"Every Dip is a Setup for a Comeback"** |
| 4 | **"We Don't Stay Down"** |
| 5 | **"오뚜기처럼, 다시. 🎎"** |

---

## 3. 토큰 이코노미 (Tokenomics)

### 3.1 총 발행량

**2,430,000,000,000 (2조 4,300억) $OTT**

발행량에는 의미가 담겨 있습니다:

```
  8,100,000,000  (현재 지구 인구 81억)
×           100  (완전한 수 — 100%의 응원)
×             3  (동양 속담: "인생에 3번은 기회가 온다")
─────────────────
= 2,430,000,000,000  — 지구의 모든 사람에게 300번의 기회를
```

- **소수점:** 6자리
- **추가 발행:** 불가 (고정 공급)
- **소각 메커니즘:** 향후 커뮤니티 투표로 결정

### 3.2 분배 구조

| 항목 | 비율 | 수량 | 용도 | 락업 |
|------|------|------|------|------|
| **유동성 풀 (LP)** | 85% | 2,065,500,000,000 | Pump.fun 본딩커브 → Raydium LP | LP 토큰 소각 (영구 잠금) |
| **에어드롭 풀** | 5% | 121,500,000,000 | NFT 민팅 가스비 + 커뮤니티 이벤트 | 없음 (운영 필요) |
| **팀** | 5% | 121,500,000,000 | 개발 및 운영 | **6개월 락업** |
| **마케팅** | 3% | 72,900,000,000 | KOL, 이벤트, 콘텐츠 제작 | 3개월 단계적 해제 |
| **커뮤니티 리저브** | 2% | 48,600,000,000 | DAO 투표, 미래 용도 | DAO 의결 시까지 잠금 |

> **참고:** Pump.fun 발행 시 초기에는 100%가 본딩커브에 진입합니다. 팀/마케팅/에어드롭 물량은 Pump.fun 졸업 후 별도 월렛에서 시장 매수로 확보하거나 사전 분배 전략을 사용합니다.

### 3.3 Pump.fun Fair Launch

$OTT는 **Pump.fun**을 통해 공정 발행(Fair Launch)됩니다. 프리세일, 프리마이닝, VC 투자가 없습니다.

**Pump.fun 본딩커브 구조:**

Pump.fun은 **상수곱 본딩커브(Constant Product Bonding Curve)**를 사용합니다:

```
가격 = k / (총공급량 - 판매량)²
```

| 항목 | 내용 |
|------|------|
| 초기 가격 | ~$0.000000001 수준 |
| 졸업 조건 | 시가총액 약 **$69,000** (약 420 SOL) 달성 |
| 매수 시 | 가격 자동 상승 (본딩커브) |
| 매도 시 | 가격 자동 하락 (본딩커브) |
| 프리세일 | **없음** |
| 프리마이닝 | **없음** |

### 3.4 Raydium 자동 상장

Pump.fun 졸업 조건(시총 ~$69K) 달성 시:

1. 본딩커브에 모인 **~79 SOL + 남은 토큰**으로 Raydium CPMM 풀 자동 생성
2. **LP 토큰 즉시 소각 (Burn)** → 유동성 **영구 잠금**
3. 이후 자유 시장에서 가격 결정
4. Jupiter, Raydium, Birdeye 등 DEX 어그리게이터에서 거래 가능

> **🔒 LP 토큰 소각은 러그풀 방지의 핵심입니다.** 소각 후에는 누구도 — 팀을 포함하여 — 유동성을 회수할 수 없습니다.

---

## 4. NFT 에어드롭 시스템

$OTT의 핵심 유틸리티: **토큰을 보유하면 응원 NFT가 자동으로 에어드롭됩니다.**

### 4.1 NFT 등급 체계 (5단계)

| 등급 | 아이콘 | 발행 한도 | 기본 확률 | 콘텐츠 유형 |
|------|--------|----------|----------|------------|
| **Common** (일반) | ⚪ | 무제한 | 80.00% | 짧은 응원 단어/메시지 (1~2단어) |
| **Rare** (희귀) | 🔵 | 무제한 | 15.00% | 1줄 응원 메시지 |
| **Epic** (영웅) | 🟣 | 무제한 | 4.50% | 2~3문장 응원 카드 (특수 디자인) |
| **Legendary** (전설) | 🟡 | **40개 한정** | 0.48% | AI 아트워크 + 유명인 명언 |
| **Mythic** (유일) | 🔴 | **3개 한정** | 0.02% | 궁극의 AI 아트워크 + 궁극 명언 |

### 4.2 Legendary (전설) 등급 상세

40개 한정, 사전 제작:

| 구분 | 수량 | 스타일 | 콘텐츠 |
|------|------|--------|--------|
| 동양풍 | 20개 | 수묵화, 민화, 우키요에, 선(禪) 아트 | 한국 전통 오뚜기 + 동양 명언/속담 |
| 서양풍 | 20개 | 팝아트, 네온, 3D, 미니멀 | 위블/다루마/펀칭백 + 서양 명언 |

- 각각 **고유한 AI 생성 이미지 + 고유 명언** 조합
- 사전 제작 후 에어드롭 시 랜덤 당첨
- 한정 수량 소진 시 Epic 등급으로 대체

### 4.3 Mythic (유일) 등급 상세

**"인생에 3번은 기회가 온다"** — 단 3개만 존재

| # | 이름 | 스타일 | 소재 |
|---|------|--------|------|
| 1 | 🥇 **Gold** | 엠보싱 금화 스타일 | 불굴의 의지 |
| 2 | 💎 **Diamond** | 크리스탈/다이아몬드 텍스처 | 빛나는 재기 |
| 3 | 🪙 **Platinum** | 양팔 만세 포즈, 플래티넘 색상 | 궁극의 승리 |

- 3개 모두 **완전히 다른 아트 디렉션, 메시지, 스타일**
- 최고 보유자 또는 특별 이벤트를 통해서만 획득 가능
- 소유자에게 **프로젝트 거버넌스 투표권** 부여

### 4.4 홀더 티어 및 에어드롭 빈도

보유량에 따라 에어드롭 빈도와 등급 보너스가 달라집니다.

| 티어 | 이모지 | 보유량 범위 | 에어드롭 빈도 | 등급 보너스 |
|------|--------|------------|-------------|------------|
| **씨앗** (Seed) | 🌱 | 10,000 ~ 99,999 | 주 1회 (일) | ×1.0 |
| **새싹** (Sprout) | 🌿 | 100,000 ~ 999,999 | 주 2회 (수/일) | ×1.5 |
| **나무** (Tree) | 🌳 | 1,000,000 ~ 99,999,999 | 주 3회 (월/수/금) | ×2.5 |
| **산** (Mountain) | 🏔 | 100,000,000 ~ 9,999,999,999 | 주 5회 (평일) | ×4.0 |
| **대지** (Earth) | 🌍 | 10,000,000,000+ | 매일 | ×6.0 |

> **최소 보유량:** 10,000 $OTT. Pump.fun 초기 가격 기준 $0.01 미만으로, 진입 장벽이 극도로 낮습니다.
> 10,000개 미만 보유자는 NFT를 받지 못합니다. 이는 스팸 방지 + 진정한 홀더 보상 목적입니다.

### 4.5 등급 보너스 확률표

등급 보너스가 높을수록 상위 등급 NFT를 받을 확률이 증가합니다.

| 등급 | 🌱 씨앗 (×1.0) | 🌿 새싹 (×1.5) | 🌳 나무 (×2.5) | 🏔 산 (×4.0) | 🌍 대지 (×6.0) |
|------|----------------|----------------|----------------|--------------|----------------|
| ⚪ Common | 80.00% | 71.50% | 56.25% | 44.00% | 44.00% |
| 🔵 Rare | 15.00% | 18.00% | 22.50% | 27.00% | 27.00% |
| 🟣 Epic | 4.50% | 8.00% | 14.00% | 21.00% | 21.00% |
| 🟡 Legendary | 0.48% | 2.30% | 6.25% | 7.20% | 7.20% |
| 🔴 Mythic | 0.02% | 0.20% | 1.00% | 0.80% | 0.80% |

> 전설/유일 등급은 **잔여 한정 수량** 내에서만 당첨됩니다. 소진 시 하위 등급으로 대체됩니다.

### 4.6 응원 메시지 데이터베이스

현재 **1,793개 메시지**가 준비되어 있습니다 (목표 초과 달성).

**등급별 분포:**

| 등급 | 한국어 | 영어 | 일본어 | 중국어 | 합계 |
|------|--------|------|--------|--------|------|
| ⚪ Common | 410 | 420 | 105 | 105 | **1,040** |
| 🔵 Rare | 200 | 200 | 50 | 50 | **500** |
| 🟣 Epic | 80 | 80 | 20 | 20 | **200** |
| 🟡 Legendary | 20 | 20 | 5 | 5 | **50** |
| 🔴 Mythic | 2 | 1 | 0 | 0 | **3** |
| **합계** | **712** | **721** | **180** | **180** | **1,793** |

**카테고리 분류:**

| 카테고리 | 수량 | 설명 |
|----------|------|------|
| 📌 Motivation | 472 | 동기부여 ("할 수 있어!") |
| 📌 Life | 389 | 인생 조언 |
| 📌 Humor | 365 | 유머 응원 ("손절은 미래의 나에게") |
| 📌 Comeback | 300 | 반등/재기 메시지 |
| 📌 Proverb | 267 | 속담/격언 |

### 4.7 자동 에어드롭 프로세스

```
매일 20:00 KST ─── 홀더 스냅샷 (보유량 스캔)
                        │
매일 21:00 KST ─── 에어드롭 실행
                        │
                  ┌─────┴─────┐
                  │ 등급 결정    │ ← 가중 랜덤 (보유량/기간 보너스)
                  └─────┬─────┘
                        │
                  ┌─────┴─────┐
                  │ 메시지 선택  │ ← 1,793개 DB에서 등급/언어별 선택
                  └─────┬─────┘
                        │
                  ┌─────┴─────┐
                  │ 이미지 생성  │ ← Common~Epic: 템플릿 / Legendary+: AI 생성
                  └─────┬─────┘
                        │
                  ┌─────┴─────┐
                  │ 메타데이터   │ ← JSON 생성 → Arweave 영구 저장
                  └─────┬─────┘
                        │
                  ┌─────┴─────┐
                  │ cNFT 민트   │ ← Metaplex Bubblegum → 홀더 지갑 전송
                  └─────┬─────┘
                        │
                  ┌─────┴─────┐
                  │ DB 기록/로그 │ ← 에어드롭 히스토리 저장
                  └───────────┘
```

---

## 5. 기술 아키텍처

### 5.1 왜 Solana인가?

| 항목 | Solana | Ethereum | Base |
|------|--------|----------|------|
| 트랜잭션 확인 | ~400ms | ~12초 | ~2초 |
| 가스비 | ~$0.00025 | ~$0.5~50 | ~$0.01 |
| cNFT 지원 | ✅ 네이티브 | ❌ | ❌ |
| 밈코인 생태계 | 🔥 활발 | 보통 | 성장 중 |
| Pump.fun 지원 | ✅ | ❌ | ❌ |

$OTT는 **대량 NFT 에어드롭**이 핵심 유틸리티입니다. Solana의 cNFT(Compressed NFT)는 일반 NFT 대비 **1,000배 저렴한 민팅 비용**으로, 대규모 에어드롭에 최적화되어 있습니다.

### 5.2 Compressed NFT (cNFT) — Metaplex Bubblegum

**cNFT vs 일반 NFT 비용 비교:**

| 비교 항목 | 일반 NFT | Compressed NFT (cNFT) |
|-----------|---------|----------------------|
| 1개 민트 비용 | ~0.01 SOL | ~0.00001 SOL |
| 1만 개 민트 | ~100 SOL | ~0.1 SOL |
| 100만 개 민트 | ~10,000 SOL | ~10 SOL |
| 마켓플레이스 지원 | ✅ | ✅ (Tensor, Magic Eden) |
| 전송 가능 | ✅ | ✅ |

**Merkle Tree 구조:**

cNFT는 **Merkle Tree** 기반으로 데이터를 압축하여 온체인 저장 비용을 획기적으로 절감합니다.

```
Merkle Tree 설정:
├── maxDepth: 14~20 (초기 14, 확장 시 20)
│   ├── depth 14: 최대 16,384개 NFT → ~0.05 SOL
│   ├── depth 17: 최대 131,072개 NFT → ~0.15 SOL
│   └── depth 20: 최대 1,048,576개 NFT → ~0.5 SOL
├── maxBufferSize: 256
├── canopyDepth: 10~14 (프루프 크기 감소, 클라이언트 부담 경감)
└── 생성: 1회성 비용
```

### 5.3 에어드롭 봇 아키텍처

```
┌─────────────────┐
│   Cron Scheduler │  ← 매일 20:00/21:00 KST 트리거
└────────┬────────┘
         │
┌────────▼────────┐
│  Holder Scanner  │  ← getTokenAccountsByMint (Solana RPC)
│                  │     전체 보유자 스캔 → 티어 분류
└────────┬────────┘
         │
┌────────▼────────┐
│ Grade Determiner │  ← 가중 랜덤 알고리즘
│                  │     보유량/기간 → 등급 보너스 적용
└────────┬────────┘
         │
┌────────▼────────┐
│ Message Selector │  ← SQLite DB (1,793개 메시지)
│                  │     등급/카테고리/언어별 선택
└────────┬────────┘
         │
┌────────▼────────┐
│  Image Pipeline  │  ← Common~Epic: 템플릿 기반
│                  │     Legendary/Mythic: AI 생성 (사전 제작)
└────────┬────────┘
         │
┌────────▼────────┐
│ Metadata Upload  │  ← JSON → Arweave 영구 저장
│                  │     이미지 → Arweave/IPFS
└────────┬────────┘
         │
┌────────▼────────┐
│  cNFT Mint &     │  ← Metaplex Bubblegum SDK
│  Transfer        │     배치 처리 (1 TX = 최대 5 cNFT)
└────────┬────────┘
         │
┌────────▼────────┐
│  DB Log &        │  ← 에어드롭 이력, 등급 통계
│  Monitoring      │     오류 시 텔레그램 알림
└─────────────────┘
```

### 5.4 등급 결정 알고리즘

```python
import random

def determine_grade(holder_balance: int, holding_days: int) -> str:
    """
    보유량과 보유기간에 따라 가중치를 적용한 등급 결정.
    """
    # 기본 확률
    base_weights = {
        'common':    80.0,
        'rare':      15.0,
        'epic':       4.5,
        'legendary':  0.48,
        'mythic':     0.02,
    }
    
    # 보유량 기반 등급 보너스
    if holder_balance >= 10_000_000_000:     # 🌍 대지
        bonus = 6.0
    elif holder_balance >= 100_000_000:      # 🏔 산
        bonus = 4.0
    elif holder_balance >= 1_000_000:        # 🌳 나무
        bonus = 2.5
    elif holder_balance >= 100_000:          # 🌿 새싹
        bonus = 1.5
    else:                                    # 🌱 씨앗
        bonus = 1.0
    
    # 보유기간 추가 보너스
    if holding_days >= 90:
        bonus *= 1.5
    elif holding_days >= 30:
        bonus *= 1.2
    
    # 가중치 조정 (상위 등급 확률 증가, Common 감소)
    adjusted = {}
    for grade, weight in base_weights.items():
        if grade == 'common':
            adjusted[grade] = weight / bonus
        else:
            adjusted[grade] = weight * bonus
    
    # 정규화 후 랜덤 선택
    total = sum(adjusted.values())
    roll = random.uniform(0, total)
    
    cumulative = 0
    for grade, weight in adjusted.items():
        cumulative += weight
        if roll <= cumulative:
            return grade
    
    return 'common'
```

### 5.5 보유자 스캔 (Holder Scanner)

```typescript
import { Connection, PublicKey } from '@solana/web3.js';

const TOTAL_SUPPLY = 2_430_000_000_000;
const MIN_BALANCE = 10_000;

interface HolderInfo {
  owner: string;
  balance: number;
  tier: string;
}

async function scanHolders(mintAddress: string): Promise<HolderInfo[]> {
  const connection = new Connection(process.env.SOLANA_RPC_URL!);
  const mint = new PublicKey(mintAddress);
  
  // 모든 토큰 계정 조회
  const accounts = await connection.getParsedProgramAccounts(
    new PublicKey('TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'),
    {
      filters: [
        { dataSize: 165 },
        { memcmp: { offset: 0, bytes: mint.toBase58() } }
      ]
    }
  );
  
  return accounts
    .map(acc => {
      const balance = acc.account.data.parsed.info.tokenAmount.uiAmount;
      return {
        owner: acc.account.data.parsed.info.owner,
        balance,
        tier: getTierName(balance),
      };
    })
    .filter(h => h.balance >= MIN_BALANCE)
    .sort((a, b) => b.balance - a.balance);
}

function getTierName(balance: number): string {
  if (balance >= 10_000_000_000) return '🌍 대지';
  if (balance >= 100_000_000)    return '🏔 산';
  if (balance >= 1_000_000)      return '🌳 나무';
  if (balance >= 100_000)        return '🌿 새싹';
  if (balance >= 10_000)         return '🌱 씨앗';
  return '자격 미달';
}
```

### 5.6 가스비 최적화 전략

| 전략 | 효과 |
|------|------|
| **cNFT 사용** | 일반 NFT 대비 1,000배 절약 |
| **배치 처리** | 1 트랜잭션에 최대 5개 cNFT 묶기 |
| **Priority Fee 동적 조절** | 네트워크 혼잡도에 따라 자동 조절 |
| **다중 RPC 엔드포인트** | Helius + QuickNode + Public RPC 분산 |
| **Merkle Tree 사전 생성** | 대형 트리 미리 생성 후 잎 노드만 추가 |
| **오프피크 실행** | 혼잡 시간대 회피 (KST 21:00 = 미국 새벽) |

### 5.7 NFT 메타데이터 구조 (Metaplex 표준)

```json
{
  "name": "OTT Cheer #12345",
  "symbol": "OTT-NFT",
  "description": "넘어져도 다시 일어나는 당신을 응원합니다 🎎",
  "image": "https://arweave.net/{TX_ID}",
  "external_url": "https://ott.fun/nft/12345",
  "attributes": [
    { "trait_type": "Grade",            "value": "Legendary" },
    { "trait_type": "Grade_Icon",       "value": "🟡" },
    { "trait_type": "Message",          "value": "Fall seven times, stand up eight." },
    { "trait_type": "Category",         "value": "proverb" },
    { "trait_type": "Language",         "value": "en" },
    { "trait_type": "Airdrop_Round",    "value": "42" },
    { "trait_type": "Recipient_Tier",   "value": "🌳 나무" }
  ],
  "properties": {
    "files": [
      { "uri": "https://arweave.net/{TX_ID}", "type": "image/png" }
    ],
    "category": "image",
    "creators": [
      { "address": "OTT_AUTHORITY_PUBKEY", "share": 100 }
    ]
  },
  "collection": {
    "name": "OTT Cheers",
    "family": "OTT"
  }
}
```

### 5.8 메타데이터 저장

| 데이터 | 저장소 | 특징 |
|--------|--------|------|
| NFT 메타데이터 (JSON) | **Arweave** | 영구 저장, 삭제 불가 |
| NFT 이미지 | **Arweave** 또는 **IPFS** | 영구 저장 |
| 에어드롭 로그 | **SQLite/PostgreSQL** | 오프체인 운영 DB |
| 메시지 DB | **SQLite** | 오프체인 |

---

## 6. 스마트 컨트랙트 및 온체인 구조

### 6.1 커스텀 Solana Program 필요 여부

| 기능 | 커스텀 프로그램 필요? | 사용 기술 |
|------|----------------------|-----------|
| 토큰 발행 | ❌ | Pump.fun / SPL Token CLI |
| NFT 민트 | ❌ | Metaplex Bubblegum SDK |
| 에어드롭 전송 | ❌ | 오프체인 스크립트 + RPC |
| 토큰 게이팅 | ❌ | 오프체인 검증 |
| DAO 거버넌스 | ⚠️ Phase 4 | SPL Governance / Realms |

> **결론:** Phase 1~3에서는 커스텀 Solana Program이 **불필요**합니다. Metaplex SDK + 오프체인 스크립트로 모든 기능을 구현합니다. 이는 스마트 컨트랙트 버그 리스크를 최소화하고, 개발 속도를 높이는 전략적 선택입니다.

### 6.2 Metaplex 활용 방안

| Metaplex 도구 | 용도 |
|---------------|------|
| **Bubblegum** | cNFT 민트/전송 (핵심) |
| **Token Metadata** | 메타데이터 표준 준수 |
| **Collection NFT** | 모든 응원 NFT를 하나의 컬렉션으로 관리 |
| **UMI 프레임워크** | Metaplex 통합 인터페이스 |

### 6.3 토큰 게이팅 로직

```typescript
// 에어드롭 자격 검증
async function verifyEligibility(wallet: string): Promise<{
  eligible: boolean;
  balance: number;
  tier: string;
  frequency: string;
  gradeBonus: number;
}> {
  const balance = await getTokenBalance(wallet, OTT_MINT);
  
  if (balance < 10_000) {
    return { eligible: false, balance, tier: 'none', frequency: 'none', gradeBonus: 0 };
  }
  
  const tiers = [
    { name: '🌍 대지', min: 10_000_000_000, freq: 'daily',    bonus: 6.0 },
    { name: '🏔 산',   min: 100_000_000,    freq: '5x/week',  bonus: 4.0 },
    { name: '🌳 나무', min: 1_000_000,      freq: '3x/week',  bonus: 2.5 },
    { name: '🌿 새싹', min: 100_000,        freq: '2x/week',  bonus: 1.5 },
    { name: '🌱 씨앗', min: 10_000,         freq: 'weekly',   bonus: 1.0 },
  ];
  
  const tier = tiers.find(t => balance >= t.min)!;
  return {
    eligible: true,
    balance,
    tier: tier.name,
    frequency: tier.freq,
    gradeBonus: tier.bonus,
  };
}
```

### 6.4 에어드롭 스케줄

```yaml
# Cron 스케줄 (KST 기준)
holder_snapshot:
  schedule: "0 20 * * *"      # 매일 20:00 KST — 스냅샷
  task: scan all holders ≥ 10,000 $OTT

airdrop_daily:
  schedule: "0 21 * * *"      # 매일 21:00 — 🌍 대지 티어
  
airdrop_5x_week:
  schedule: "0 21 * * 1-5"    # 평일 — 🏔 산 티어

airdrop_3x_week:
  schedule: "0 21 * * 1,3,5"  # 월/수/금 — 🌳 나무 티어

airdrop_2x_week:
  schedule: "0 21 * * 3,0"    # 수/일 — 🌿 새싹 티어

airdrop_weekly:
  schedule: "0 21 * * 0"      # 일요일 — 🌱 씨앗 티어
```

---

## 7. 웹사이트 및 프론트엔드

### 7.1 랜딩 페이지 구성

```
ott.fun/
├── 🎯 Hero Section
│   ├── 오뚜기 캐릭터 애니메이션 (넘어졌다 일어남)
│   ├── 슬로건: "넘어져도 다시 일어나는 코인 🎎"
│   ├── [Buy on Raydium] [Join Telegram] CTA 버튼
│   └── 실시간 가격 + 시가총액
│
├── 📖 About Section
│   ├── 프로젝트 소개 + 비전
│   └── 왜 오뚜기인가?
│
├── 🎨 NFT Gallery
│   ├── 최근 에어드롭 NFT 미리보기
│   ├── 등급별 필터 (Common~Mythic)
│   └── [내 NFT 보기] (Phantom 월렛 연결)
│
├── 📡 Live Airdrop Feed
│   ├── 실시간 에어드롭 로그 (WebSocket)
│   ├── "🎎 Wallet 7x...3k received 🟡 Legendary!"
│   └── 등급별 통계 차트
│
├── 📊 Tokenomics
│   ├── 분배 구조 파이차트
│   ├── 본딩커브/LP 상태
│   └── Contract Address (복사 버튼)
│
├── 🗺️ Roadmap
│   └── 인터랙티브 타임라인
│
└── Footer
    ├── Telegram | X | GitHub
    ├── Contract Address (복사)
    └── "Made with ❤️ by OTT Team"
```

### 7.2 기술 스택 (웹)

| 항목 | 기술 |
|------|------|
| 프레임워크 | Next.js 14 (Static Export) |
| 스타일 | Tailwind CSS |
| 월렛 연결 | `@solana/wallet-adapter-react` |
| cNFT 조회 | Helius DAS API |
| 실시간 피드 | WebSocket / Server-Sent Events |
| 배포 | GitHub Pages (정적) 또는 Vercel |

### 7.3 NFT 갤러리 기능

- Phantom 월렛 연결 → DAS API로 해당 월렛의 OTT cNFT 조회
- 등급별 필터, 시간순/등급순 정렬
- NFT 클릭 → 상세 정보 (메시지, 등급, 에어드롭 일시, 라운드)
- X/텔레그램 공유 기능
- 전체 보유자 순위 (Top 10)

---

## 8. 커뮤니티 전략

### 8.1 텔레그램

**메인 그룹:**
- 한국어/영어 혼용 채팅
- 스캠 방지 봇, 링크 제한, 신규 멤버 캡차
- 주간 밈 대회, AMA, 커뮤니티 투표

**공지 채널:**
- 에어드롭 결과, 업데이트, 로드맵 진행 상황

**텔레그램 봇 명령어:**

| 명령어 | 기능 |
|--------|------|
| `/balance <wallet>` | 보유량 확인 |
| `/mynft` | 내 NFT 컬렉션 |
| `/stats` | 전체 통계 (보유자 수, NFT 발행량) |
| `/nextdrop` | 다음 에어드롭까지 남은 시간 |
| `/grade` | 내 등급/티어 확인 |
| `/leaderboard` | 보유량 TOP 10 |

### 8.2 X (Twitter) 전략

1. **밈 콘텐츠:** 오뚜기 캐릭터 + 크립토 밈 조합
2. **에어드롭 알림:** 매 에어드롭마다 자동 트윗
3. **RT 이벤트:** RT + 팔로우 → 추가 NFT 에어드롭
4. **KOL 협업:** 솔라나 밈코인 인플루언서 접촉
5. **해시태그:** `#OTT` `#넘어져도다시` `#OttCoin` `#SolanaMeme`

### 8.3 밈 콘텐츠 계획

- 오뚜기 캐릭터 시리즈 (다양한 상황에서 넘어졌다 일어남)
- 시장 하락 시 "오뚜기 타임" 밈 자동 생성
- GIF/숏폼 영상 (오뚜기 넘어지고 일어나는 애니메이션)
- 커뮤니티 밈 대회 (주간, 우승자 Legendary NFT)

---

## 9. 로드맵

### Phase 1: 탄생 — Genesis (Week 1~2)

- [ ] $OTT 토큰 Pump.fun 발행
- [ ] 로고 및 브랜드 아이덴티티 확립
- [ ] 랜딩 페이지 (ott.fun) 배포
- [ ] 텔레그램 그룹 + 봇 개설
- [ ] X(트위터) 계정 + 초기 밈 콘텐츠
- [ ] CoinGecko / DexScreener 등록

### Phase 2: 응원 시작 — Cheers Begin (Week 3~6)

- [ ] Merkle Tree 생성 + cNFT 시스템 구축
- [ ] 자동 에어드롭 봇 개발 + 테스트넷 검증
- [ ] 메인넷 에어드롭 가동
- [ ] NFT 갤러리 페이지 오픈
- [ ] 텔레그램 봇 고도화

### Phase 3: 성장 — Growth (Month 2~4)

- [ ] 1,000+ 홀더 달성
- [ ] DEX Screener 트렌딩 진입
- [ ] KOL 마케팅 캠페인
- [ ] NFT 마켓플레이스 연동 (Tensor, Magic Eden)
- [ ] 커뮤니티 거버넌스 투표 시스템 도입

### Phase 4: 확장 — Expansion (Month 4+)

- [ ] 멀티체인 확장 (Base, Ethereum L2)
- [ ] 파트너십 (밈코인/NFT 프로젝트)
- [ ] 실물 굿즈 (오뚜기 피규어, 스티커)
- [ ] 모바일 앱 (NFT 월렛 + 응원 알림)
- [ ] DAO 전환 — 커뮤니티 주도 운영

---

## 10. 비용 구조 및 운영 투명성

투명성을 위해 모든 예상 비용을 공개합니다.

### 10.1 초기 셋업 비용

| 항목 | 비용 (SOL) | 비용 (USD) | 비고 |
|------|-----------|-----------|------|
| Pump.fun 토큰 발행 | 0.02 | ~$3 | 1회성 |
| Merkle Tree 생성 (depth 14) | 0.05 | ~$7.5 | 1회성, 16,384개 용량 |
| 도메인 (ott.fun) | - | ~$15/년 | .fun 도메인 |
| **초기 합계** | **~0.1 SOL** | **~$25** | |

### 10.2 월간 운영 비용

| 항목 | 비용 (SOL) | 비용 (USD) | 비고 |
|------|-----------|-----------|------|
| cNFT 민팅 (월 3만 개 기준) | 0.3 | ~$45 | ~0.00001 SOL/개 |
| Arweave 메타데이터 저장 | 0.1 | ~$15 | JSON 업로드 |
| Helius RPC (Pro) | - | $49 | DAS API + Enhanced RPC |
| 서버 호스팅 | - | ~$5 | 에어드롭 봇 |
| AI 이미지 (Legendary/Mythic) | - | ~$12 | OpenAI gpt-image-1 |
| **월간 합계** | **~0.4 SOL** | **~$126** | |

### 10.3 확장 시 비용

| 항목 | 트리거 | 추가 비용 |
|------|--------|----------|
| Merkle Tree 추가 (depth 20) | 16,384개 소진 시 | ~0.5 SOL (1회) |
| RPC 업그레이드 | 보유자 10,000+ | $99/월 |
| 서버 스케일업 | 트래픽 증가 | $20~50/월 |

---

## 11. 리스크 분석

### 11.1 기술적 리스크

| 리스크 | 심각도 | 확률 | 대응 방안 |
|--------|--------|------|-----------|
| Solana 네트워크 다운타임 | 중 | 낮 | 에어드롭 큐잉 후 재시도 |
| RPC 레이트 리밋 | 중 | 중 | 다중 RPC (Helius + QuickNode + Public) |
| Merkle Tree 용량 초과 | 낮 | 낮 | 새 트리 생성 (확장 가능) |
| 에어드롭 봇 장애 | 중 | 중 | 모니터링 + 자동 재시작 + 알림 |
| 메타데이터 스토리지 장애 | 낮 | 낮 | Arweave (영구 저장) 사용 |
| 프라이빗 키 유출 | 높 | 낮 | 하드웨어 월렛 + 환경변수 암호화 |

### 11.2 시장 리스크

| 리스크 | 심각도 | 대응 방안 |
|--------|--------|-----------|
| 극단적 가격 변동 | 높 | LP 소각으로 최소 유동성 보장, 수익 약속 없음 |
| 유동성 부족 | 높 | Pump.fun → Raydium 자동 상장, LP 영구 잠금 |
| 밈코인 시장 냉각 | 중 | NFT 유틸리티로 차별화, 장기 보유 인센티브 |
| 경쟁 프로젝트 출현 | 중 | 독특한 컨셉(응원/격려) + 커뮤니티 충성도 |
| SOL 가격 하락 | 중 | 운영비 일부 스테이블코인 보유 |

### 11.3 규제 리스크

| 리스크 | 심각도 | 대응 방안 |
|--------|--------|-----------|
| 증권성 판단 | 높 | 수익 약속 없음, 유틸리티(NFT) 강조, 탈중앙 구조 |
| 각국 가상자산법 변경 | 중 | 글로벌 DEX 중심 운영, 규제 동향 모니터링 |
| NFT 에어드롭 과세 | 중 | 면책 조항에 과세 가능성 고지 |
| 한국 가상자산법 | 중 | 한국 거래소 상장 지양, DEX 중심 |

---

## 12. 기술 스택 총정리

### 12.1 개발 언어 및 프레임워크

| 분류 | 기술 | 용도 |
|------|------|------|
| **메인 언어** | TypeScript | 에어드롭 봇, 텔레그램 봇, 웹 |
| **보조 언어** | Python | AI 이미지 생성, 데이터 분석, 메시지 DB 관리 |
| **프론트엔드** | Next.js 14 | 웹사이트 (Static Export) |
| **스타일** | Tailwind CSS | UI |
| **백엔드** | Node.js 20+ | 에어드롭 봇, 텔레그램 봇 |
| **DB** | SQLite | 메시지 DB, 에어드롭 로그 |

### 12.2 블록체인 SDK

| 라이브러리 | 용도 |
|-----------|------|
| `@solana/web3.js` 2.x | Solana 기본 상호작용 |
| `@metaplex-foundation/mpl-bubblegum` | cNFT 민트 |
| `@metaplex-foundation/mpl-token-metadata` | NFT 메타데이터 |
| `@metaplex-foundation/umi` | Metaplex 통합 프레임워크 |
| `@solana/spl-token` | SPL 토큰 조작 |
| `@solana/wallet-adapter-react` | 웹 월렛 연결 |

### 12.3 외부 API/서비스

| API | 용도 | 비용 |
|-----|------|------|
| **Helius** DAS API + RPC | cNFT 조회, 보유자 스캔 | $49/월 (Pro) |
| **OpenAI** gpt-image-1 | Legendary/Mythic 이미지 생성 | $0.04/image |
| **Arweave** (Irys) | 메타데이터/이미지 영구 저장 | ~$0.001/upload |
| **CoinGecko** API | 가격 정보 | 무료 |
| **Birdeye** API | DEX 가격/차트 | 무료 |

### 12.4 인프라 도구

| 도구 | 용도 |
|------|------|
| `node-cron` | 에어드롭 스케줄링 |
| `grammY` | 텔레그램 봇 프레임워크 |
| `sharp` | 이미지 처리 (텍스트 오버레이) |
| `winston` | 로깅 |
| GitHub Pages / Vercel | 웹사이트 배포 |

### 12.5 개발 환경

```
필수:
  Node.js >= 20.0.0
  npm >= 10.0.0
  Solana CLI >= 1.18
  Python >= 3.10
  Git

환경변수:
  SOLANA_RPC_URL       = Helius RPC URL
  HELIUS_API_KEY       = Helius API Key
  OTT_MINT             = 토큰 민트 주소
  AUTHORITY_KEYPAIR    = 운영 키페어 경로
  OPENAI_API_KEY       = OpenAI API Key
  TELEGRAM_BOT_TOKEN   = 텔레그램 봇 토큰
  ARWEAVE_WALLET       = Arweave 월렛 경로
  DATABASE_URL         = sqlite:./data/ott.db
```

---

## 13. 팀

$OTT는 **익명 팀**에 의해 개발 및 운영됩니다.

크립토 생태계의 전통에 따라 팀 구성원의 개인 정보는 공개하지 않습니다. 대신 **코드와 실행**으로 신뢰를 증명합니다.

### 투명성 보장 수단

| 항목 | 설명 |
|------|------|
| **오픈소스** | 에어드롭 봇 및 웹사이트 코드 GitHub 공개 |
| **온체인 검증** | 모든 토큰 분배/에어드롭은 온체인에서 확인 가능 |
| **LP 소각** | 유동성 풀 토큰 소각 → 러그풀 방지 |
| **팀 물량 락업** | 팀 토큰 6개월 락업 |
| **운영비 공개** | 백서에 모든 비용 구조 투명 공개 |
| **커뮤니티 소통** | 텔레그램/X를 통한 투명한 소통 |

### 연락처

| 채널 | 링크 |
|------|------|
| Telegram | [추후 공개] |
| X (Twitter) | [추후 공개] |
| Website | ott.fun |
| GitHub | [추후 공개] |

---

## 14. 부록

### 14.1 프로젝트 디렉토리 구조

```
ott/
├── apps/
│   ├── web/                 # Next.js 웹사이트
│   ├── airdrop-bot/         # 에어드롭 자동화 봇
│   └── telegram-bot/        # 텔레그램 봇
├── packages/
│   ├── core/                # 공유 유틸리티 (등급 결정, DB 등)
│   ├── solana/              # Solana 상호작용 래퍼
│   └── types/               # 공유 타입 정의
├── data/
│   ├── messages/            # 응원 메시지 DB
│   ├── images/              # 템플릿/생성 이미지
│   └── ott.db               # SQLite DB
├── scripts/
│   ├── setup-merkle-tree.ts
│   ├── seed-messages.ts
│   └── test-airdrop.ts
├── docs/
│   ├── WHITEPAPER.md
│   └── WHITEPAPER_EN.md
├── .env.example
├── package.json
└── turbo.json               # Turborepo 모노레포
```

### 14.2 메시지 DB 스키마

```sql
CREATE TABLE cheer_messages (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    grade       TEXT NOT NULL CHECK(grade IN ('common','rare','epic','legendary','mythic')),
    category    TEXT NOT NULL,      -- motivation, proverb, humor, life, comeback
    language    TEXT NOT NULL,      -- ko, en, ja, zh
    message     TEXT NOT NULL,
    source      TEXT,               -- 출처 (인물명 등, nullable)
    used_count  INTEGER DEFAULT 0,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_grade_lang ON cheer_messages(grade, language);
CREATE INDEX idx_category ON cheer_messages(category);
```

### 14.3 용어 정리

| 용어 | 설명 |
|------|------|
| **cNFT** | Compressed NFT. Merkle Tree 기반으로 압축된 NFT. 민팅 비용 극소화. |
| **Merkle Tree** | 해시 트리 구조. 대량 데이터를 효율적으로 검증하는 데이터 구조. |
| **Bubblegum** | Metaplex의 cNFT 프로그램. Solana에서 cNFT를 민트/전송하는 표준. |
| **Pump.fun** | Solana 밈코인 Fair Launch 플랫폼. 본딩커브 기반. |
| **Raydium** | Solana DEX. Pump.fun 졸업 시 자동 상장. |
| **LP 소각** | 유동성 풀 토큰을 영구 소멸시켜 러그풀을 방지하는 행위. |
| **Fair Launch** | 프리세일/프리마이닝 없이 모든 참여자에게 동일 조건으로 시작하는 발행 방식. |
| **DAS API** | Digital Asset Standard API. Helius가 제공하는 cNFT 조회 API. |
| **SPL Token-2022** | Solana의 최신 토큰 표준. 확장 기능 지원. |
| **Arweave** | 영구 저장 블록체인. 한번 저장하면 삭제 불가. |
| **DYOR** | Do Your Own Research. 독립적 리서치를 수행하라는 의미. |

---

*$OTT — 넘어져도 다시 일어나는 코인 🎎*

*Fall Seven Times, Stand Up Eight. 七転八起*

---

*본 문서는 $OTT 프로젝트의 현재 계획을 설명하며, 향후 변경될 수 있습니다.*  
*본 문서는 투자 조언이 아닙니다. 모든 투자 결정은 개인의 책임입니다.*  
*$OTT 토큰 구매 시 본 백서의 면책 조항에 동의한 것으로 간주합니다.*

*© 2026 OTT Project. All rights reserved.*
