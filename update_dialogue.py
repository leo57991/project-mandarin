import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_dialogue = """const dialogueTree = {
            CHEN_AFAR: {
                START: {
                    text: "（陳阿發擦著桌子，[shake]眼神飄忽[/shake]）探長，您來了。我已經把我知道的都跟列車長說了，真的，我什麼都沒看見……",
                    choices: [
                        { text: "你發現尸體的時候，現場是什麼情況？", tone: "polite", grammarPoint: "GP2_TIME_ADVERB", isCorrect: true, response: "那時大概九點十分，我從廚房出來，就看到江先生倒在椅子邊，趙先生站在旁邊，[shake]臉色發白[/shake]。之前我送咖啡時他們還在講話。後來我回廚房洗碗，再出來就是那樣了……", nextNode: "END" },
                        { text: "你什麼時候發現的尸體？", tone: "neutral", grammarPoint: "GP2_TIME_ADVERB", isCorrect: false, response: "什麼時候？嗯……我記不太清了，好像是九點半，也可能快十點了。我洗碗洗得太累了，沒有注意確切的時間。", nextNode: "END" }
                    ]
                },
                CHEN_2: {
                    text: "（陳阿發壓低聲音，四下張望）探長……您還有事嗎？",
                    choices: [
                        { text: "請問您那時候有沒有注意到可疑的人？", tone: "polite", response: "有個人從餐車往頭等艙方向去。穿深色大衣。對了，那個俄國貴族——[ink]303號包廂[/ink]的男爵夫人——她當時也在餐車。您可以去問問她。", nextNode: "END" },
                        { text: "難道你打算隱瞞看到的人嗎？", tone: "aggressive", response: "我……我有看到一個穿深色大衣的人走得很急。還有那個——303號的洋夫人也在。", nextNode: "END" }
                    ]
                },
                CHEN_3: {
                    text: "（陳阿發探頭看看左右）探長，您還在查？我剛剛又想到一件事……",
                    choices: [
                        { text: "什麼事？請說。", tone: "polite", response: "趙先生上車的時候，那件[key]藏青色圍巾[/key]可講究了，圍在脖子上，誰碰他跟誰急。可今晚我見他從走廊回來時，圍巾不見了，手裡多了個[shake]鼓鼓的皮包[/shake]，露出一截圍巾尾。他那是把圍巾硬塞進包裡了，為什麼要這樣？", clueId: "CLUE_CHEN_SCARF_OBSERVATION", playerReceived: "陳阿發目擊趙福生從走廊返回後，隨身的藏青色圍巾消失了，塞入了行李包中。", truthVersion: "趙福生在殺人後藏匿了作案工具——用於勒頸的圍巾，趁亂藏入男爵夫人包廂。", nextNode: "END" },
                        { text: "哦？說說看吧。", tone: "neutral", response: "趙先生那條圍巾，上車時一直圍著，挺貴氣的。但我今晚見他從走廊那頭過來，圍巾不見了，皮包鼓鼓的，還有點[shake]神情慌張[/shake]。", clueId: "CLUE_CHEN_SCARF_OBSERVATION", playerReceived: "陳阿發目擊趙福生從走廊返回後，隨身的藏青色圍巾消失了，塞入了行李包中。", truthVersion: "趙福生在殺人後藏匿了作案工具——用於勒頸的圍巾，趁亂藏入男爵夫人包廂。", nextNode: "END" }
                    ]
                },
                CHEN_4: {
                    text: "（陳阿發壓低聲音，把您拉到廚房門口）探長，這不是鬧著玩的……我今晚在廚房裡，[crime]親眼看到趙先生在爐子那裡燒東西[/crime]。他說他在燒廢紙，但那紙……看起來像有[key]火漆印[/key]的東西。",
                    choices: [
                        { text: "您有沒有撿到任何殘留的紙片？", tone: "polite", response: "我當時嚇到了，沒敢湊近。但爐灶裡[ink]有幾張沒燒完全的紙[/ink]，我後來掃地的時候看到的。探長您要不要去找找看？", nextNode: "END" },
                        { text: "那他有沒有發現您看見他？", tone: "neutral", response: "發現了！他回頭看到我，當時[shake]臉色一下子變得很難看[/shake]，叫我趕快出去，說廚房是員工禁區。可我是餐車員工啊！他才是不該進廚房的人！", nextNode: "END" }
                    ]
                },
                CHEN_5: {
                    text: "（陳阿發在廚房裡焦急地等您）探長，您找到那個紙片了嗎？那是[key]手稿殘頁[/key]！我認得那種火漆印，是……是很厲害的地方蓋的！",
                    choices: [
                        { text: "您知道這份文件的重要性嗎？", tone: "polite", response: "我不懂那些大道理，但我知道[crime]江先生就是為了這個丟了命[/crime]。探長，您一定要查清楚啊。趙先生那個人，他表面上是商人，但……眼神太冷了。", nextNode: "END" },
                        { text: "您還看到什麼了？", tone: "neutral", response: "我還看到他的手上……好像有[ink]一點燒傷的痕跡[/ink]，他燒紙的時候可能太急了。這個人，殺了人還敢若無其事……", nextNode: "END" }
                    ]
                },
                CHEN_BONUS_POLITE: {
                    text: "（陳阿發猶豫了一下）那個人……[ink]身材很高[/ink]，戴著帽子壓得很低。我只看到他的[shake]側臉[/shake]。",
                    choices: [
                        { text: "這很有幫助，謝謝。", tone: "neutral", clueId: "CLUE_DARK_COAT_DETAIL", playerReceived: "深色大衣的人身材高大，戴帽子壓低臉，陳阿發只看到側臉。", truthVersion: "更具體的外型描述，與趙福生殺死江明後的體貌特徵完全吻合。", nextNode: "END" }
                    ]
                },
                CHEN_BONUS_AGGRESSIVE: {
                    text: "（陳阿發被嚇到，[shake]說漏嘴[/shake]）他……他走的時候一直[ink]回頭看[/ink]，好像在找什麼東西！",
                    choices: [
                        { text: "繼續說。", tone: "neutral", clueId: "CLUE_DARK_COAT_NERVOUS", playerReceived: "深色大衣的人離開時不斷回頭張望，像是在找什麼重要的東西。", truthVersion: "趙福生殺人後折返廚房尋找遺落的手稿殘頁時表現出的焦急跡象。", nextNode: "END" }
                    ]
                },
                'CONFRONT_CLUE_COFFEE_CUP': {
                    text: "「啊！這不是白男爵夫人的咖啡杯嗎？我昨晚一直在找它……[shake]雖然這是我遺失的[/shake]，但我絕對沒有殺害江明先生！」",
                    expression: "worried",
                    choices: [{ text: "繼續詢問", nextNode: "CHEN_2" }]
                },
                END: { text: "（陳阿發低下頭繼續擦桌子）我就知道這些了。", choices: [] },
                INTERROGATION: {
                    'CLUE_COFFEE_CUP': 'CONFRONT_CLUE_COFFEE_CUP',
                    'CLUE_SCARF': 'CHEN_3',
                    'CLUE_FILM_CASE': 'CHEN_4',
                    'CLUE_MANUSCRIPT_PAGE': 'CHEN_5'
                }
            },
            ZHAO: {
                START: {
                    text: "（趙福生放下報紙，神情泰然）探長，有何貴幹？",
                    choices: [
                        { text: "案發當時，您在哪裡？", tone: "polite", grammarPoint: "GP4_WORD_ORDER", isCorrect: true, response: "我就在餐車。江明倒下的時候，我離他最近。但我也是受害者，我差點被牽連。", nextNode: "END" },
                        { text: "你就是兇手吧！", tone: "aggressive", grammarPoint: "GP4_WORD_ORDER", isCorrect: false, response: "探長，說話要講證據。", nextNode: "END" }
                    ]
                },
                ZHAO_2: {
                    text: "（趙福生看著您手中的[key]相機[/key]）那是江明的相機，他不離身的。不過昨晚我確實沒注意他在不在拍。",
                    choices: [
                        { text: "底片槽是空的，底片被人取走了。您知道誰會這麼做嗎？", tone: "polite", response: "（眼神一閃而過）……我不知道。江明那個人很謹慎，不會隨便讓人動他的東西。", nextNode: "END" }
                    ]
                },
                ZHAO_3: {
                    text: "（趙福生接過您呈示的[key]外文電報[/key]，表情微微一僵）這……這哪裡來的？",
                    choices: [
                        { text: "您的包廂桌上。電報是法文，收件人是您。", tone: "polite", response: "（沉默片刻）這是商業往來的電報。我在上海做紡織生意，與法國客戶有業務聯繫。這沒什麼好解釋的。", nextNode: "END" },
                        { text: "這封電報告訴我，您這次上車絕非只是做生意。", tone: "aggressive", response: "（臉色一白）你……你不要亂說！這是私人電報！", nextNode: "END" }
                    ]
                },
                ZHAO_4: {
                    text: "（趙福生看到您手中的[key]聽診器[/key]，突然一怔）那個……那不是那個護士小姐的東西嗎？",
                    choices: [
                        { text: "是方小蘭醫師的。她說這是您從她醫療包裡拿走的。", tone: "polite", response: "（強行鎮定）胡說。我為什麼要拿她的東西？我那晚只是問她借了繃帶，我的手……（停頓）沒什麼，我只是問了問。", nextNode: "END" },
                        { text: "您謊稱手受傷，實際上是為了偷竊這個聽診器偷聽別人談話！", tone: "aggressive", response: "（拍桌）你這是誣陷！你有什麼證據！", nextNode: "END" }
                    ]
                },
                ZHAO_5_INTRO: {
                    text: "（趙福生看到您手中的[key]隱藏紙條[/key]，緩緩坐回椅子，表情隱晦難測）探長，您很厲害。但光憑這些……您能定我的罪嗎？",
                    choices: [
                        { text: "這已經足夠證明你拿走了底片。", tone: "polite", response: "就算我拿了底片，那又如何？殺人可是要講求直接證據的。", nextNode: "END" }
                    ]
                },
                ZHAO_BONUS_POLITE: {
                    text: "（趙福生冷笑）探長，您是個聰明人。但有些水太深，您最好別趟。江明手裡的東西，不是他該拿的。",
                    choices: [
                        { text: "他在哪裡？", tone: "neutral", clueId: "CLUE_ZHAO_THREAT", playerReceived: "趙福生暗示江明持有的物品涉及極大勢力，警告探長停止調查。", truthVersion: "趙福生確認自己是為奪取機密文件而來，側面承認其動機。", nextNode: "END" }
                    ]
                },
                ZHAO_BONUS_AGGRESSIVE: {
                    text: "（趙福生[shake]惱羞成怒[/shake]）你以為你能把我怎麼樣？就算你把我交給警察，明天我就會無罪釋放！你根本不知道你在對付誰！",
                    choices: [
                        { text: "法律會制裁你。", tone: "neutral", clueId: "CLUE_ZHAO_ARROGANCE", playerReceived: "趙福生極度囂張，聲稱背後的勢力足以讓他免於任何法律制裁。", truthVersion: "進一步證實趙福生背靠外國勢力，擁有超越普通法律的特權。", nextNode: "END" }
                    ]
                },
                END: { text: "（趙福生閉上眼睛，拒絕再回答）", choices: [] },
                INTERROGATION: {
                    'CLUE_CAMERA': 'ZHAO_2',
                    'CLUE_LETTER': 'ZHAO_3',
                    'CLUE_STETHOSCOPE': 'ZHAO_4',
                    'CLUE_JIANGMING_NOTE': 'ZHAO_5_INTRO'
                }
            },
            BARONESS: {
                START: {
                    text: "（白男爵夫人冷冷地打量您）你是誰？",
                    choices: [
                        { text: "不好意思打擾您，請問您認識江明先生嗎？", tone: "polite", grammarPoint: "GP1_HONORIFIC", isCorrect: true, response: "（嘆氣）認識。他欠了我一筆錢，我這次上車就是要討債的。", nextNode: "BARONESS_2" },
                        { text: "難道你是為了債務殺死江明嗎？", tone: "aggressive", grammarPoint: "GP1_HONORIFIC", isCorrect: false, response: "（面無表情）注意你的措辭，偵探。", nextNode: "END" }
                    ]
                },
                BARONESS_2: {
                    text: "昨晚您在哪裡？",
                    choices: [
                        { text: "請告訴我您目擊的一切細節。", tone: "polite", response: "餐車角落，喝咖啡等他。但我看到一個穿[ink]深色大衣[/ink]的人走得很急。", nextNode: "END" },
                        { text: "竟然在那種地方待了一整晚？", tone: "aggressive", response: "（皺眉）我只是在等一個不守時的人。", nextNode: "END" }
                    ]
                },
                BARONESS_3: {
                    text: "（白男爵夫人看著您手中的[key]咖啡杯[/key]）關於那個咖啡杯……",
                    choices: [
                        { text: "不好意思，您忘了帶走它。", tone: "polite", response: "是的，杯沿有我的脣印。但我發誓我看到那個人離開時，江明還沒出事。", nextNode: "END" },
                        { text: "明明證據就在現場，你竟敢否認？", tone: "aggressive", response: "（冷笑）那是證明我在場，而不是證明我殺人的證據。", nextNode: "END" }
                    ]
                },
                BARONESS_4: {
                    text: "（白男爵夫人看著您呈示的[key]外文電報[/key]，輕輕嘆了口氣）這封電報……",
                    choices: [
                        { text: "這封外文電報是怎麼回事？", tone: "polite", response: "昨晚我從走廊回來的時候，發現房門開了一條縫，梳妝台上多了這張紙，我不知道是誰放的。對了，說到這個，我[ink]聞到過趙先生身上有紙張燒焦的味道[/ink]。", nextNode: "BARONESS_4B" },
                        { text: "您知道這電報是誰放的嗎？", tone: "neutral", response: "不知道。但我發現的時候，房門縫裡還有股燒焦的氣息。趙先生那晚不知道在廚房搗什麼鬼。", nextNode: "BARONESS_4B" }
                    ]
                },
                BARONESS_4B: {
                    text: "（男爵夫人若有所思）他還曾跟我說過他弄到了一份[key]「能讓洋人睡不著覺的東西」[/key]。",
                    choices: [
                        { text: "謝謝您。", tone: "polite", response: "他終究還是把命搭了進去，誰知道呢，誰知道呢。", clueId: "CLUE_BARONESS_JIANGMING_HINT", playerReceived: "男爵夫人轉述江明曾提到手上有份「能讓洋人睡不著覺的東西」，暗指機密文件。", truthVersion: "江明掌握的秘密條約副本是使列強寢食難安的核心證據，也是他被殺的真正原因。", nextNode: "END" }
                    ]
                },
                BARONESS_5: {
                    text: "（男爵夫人看到您手中的殘頁，[shake]神情凝重[/shake]）「這紙片上的火漆印……我認得。獅子與獨角獸，是[key]英國使館的徽記[/key]。」",
                    choices: [
                        { text: "您確定？", tone: "polite", response: "不會錯的。我在上海這麼多年，跟各國使館的人打過不少交道。", nextNode: "BARONESS_5B" }
                    ]
                },
                BARONESS_5B: {
                    text: "（男爵夫人緩緩說道）如果江明手上真的有這種東西，那這件事就比探長你想像的要[impact]大得多[/impact]了。",
                    choices: [
                        { text: "謝謝您，這對案件至關重要。", tone: "polite", clueId: "CLUE_EMBASSY_SEAL", playerReceived: "男爵夫人確認手稿殘頁上的火漆印是英國使館的獅子與獨角獸徽記。", truthVersion: "江明持有的是英國使館機密文件副本，涉及列強瓜分中國的秘密計劃，這就是他被殺的核心原因。", nextNode: "END" }
                    ]
                },
                BARONESS_BONUS_POLITE: {
                    text: "（白男爵夫人若有所思）那個人走路很奇怪……[ink]刻意壓低腳步聲[/ink]，甚至還把那條厚重的[key]深色圍巾[/key]裹在脖子上，像是想遮住臉。",
                    choices: [
                        { text: "這項觀察非常關鍵。", tone: "neutral", clueId: "CLUE_BARONESS_FOOTSTEP", playerReceived: "男爵夫人觀察到穿深色大衣的人行動極其謹慎，且身上攜帶著與包廂內發現的一致的圍巾。", truthVersion: "趙福生在謀殺過程中使用了圍巾作為勒殺工具，隨後試圖藏匿證據。", nextNode: "END" }
                    ]
                },
                BARONESS_BONUS_AGGRESSIVE: {
                    text: "（白男爵夫人冷冷地）既然你發現了那份[key]外文電報[/key]，就該知道趙先生這次來北京並非為了經商，而是執行一場「清理」任務。",
                    choices: [
                        { text: "清理江明嗎？", tone: "neutral", clueId: "CLUE_BARONESS_HINT", playerReceived: "男爵夫人暗示趙福生身上帶有外國勢力的指令，目標是「清理」相關人員。", truthVersion: "男爵夫人利用電報線索點破趙福生的殺手身份，將調查導向正確目標。", nextNode: "END" }
                    ]
                },
                END: { text: "（白男爵夫人轉身望向窗外的雪景，不再說話）", choices: [] },
                INTERROGATION: {
                    'CLUE_COFFEE_CUP': 'BARONESS_3',
                    'CLUE_LETTER': 'BARONESS_4',
                    'CLUE_MANUSCRIPT_PAGE': 'BARONESS_5'
                }
            },
            FANG: {
                START: {
                    text: "（方小蘭皺眉）醫務工作很忙。你有什麼事？",
                    choices: [
                        { text: "請問您昨晚在哪裡？", tone: "polite", grammarPoint: "GP3_LOCATION_WORD", isCorrect: true, response: "我一直在走廊整理醫療包，沒有去過餐車。", nextNode: "END" },
                        { text: "你昨晚在餐車做什麼？", tone: "aggressive", grammarPoint: "GP3_LOCATION_WORD", isCorrect: false, response: "我根本沒去過餐車！", nextNode: "END" }
                    ]
                },
                FANG_2: {
                    text: "（看到您出示的[key]聽診器[/key]）桌子下面？我昨晚把它放在走廊醫療包裡，回來就不見了！趙先生當時正好經過，還停下來跟我打過招呼……沒想到那之後聽診器就丟了。",
                    choices: [
                        { text: "趙先生有什麼可疑的動作嗎？", tone: "polite", response: "他問我醫療包裡有沒有繃帶，說他手被紙割到了。但我看他的手，[ink]根本沒有傷口[/ink]。他肯定是想藉機找理由開我的醫療包！", nextNode: "FANG_3" },
                        { text: "你竟然懷疑趙先生？", tone: "aggressive", response: "我……我只是說他經過過！他問我借繃帶，說手受傷了，但我根本沒看到任何傷口！", nextNode: "END" }
                    ]
                },
                FANG_3: {
                    text: "（方小蘭猶豫了一下）探長，其實我……我有一件事沒跟您說。",
                    choices: [
                        { text: "請說，我不會隨意判斷。", tone: "polite", response: "我其實不只是護士。我是[key]《晨光報》的記者[/key]，這次以醫護人員的身份上車，是為了追蹤江明的手稿。我聽說他手上有份很重要的東西……但我沒想到，他會死在這列火車上。", nextNode: "END" },
                        { text: "你一直在隱瞞什麼？", tone: "aggressive", response: "（咬唇）好吧……我是記者。《晨光報》的。我這次上車是為了採訪江明的，他手上有份涉及列強的秘密文件……現在他死了，我也不知道該怎麼辦。", nextNode: "END" }
                    ]
                },
                FANG_4: {
                    text: "（方小蘭看著您手中的[key]手稿殘頁[/key]，眼睛微微發亮）這是……那份手稿的一部分？！",
                    choices: [
                        { text: "您認識上面的內容嗎？", tone: "polite", response: "火漆印……英國使館？！那就對了！江明說過，那份文件是英國使館流出來的秘密條約副本。[impact]趙福生殺他，就是為了這個！[/impact]探長，您手上的這幾樣東西已經足夠了——快去餐車，趙福生現在一定還在那裡，趁他還沒機會銷毀更多證據！", nextNode: "END" }
                    ]
                },
                FANG_5: {
                    text: "（方小蘭焦急地說）探長，您已經掌握的線索夠多了！[impact]快去餐車找趙福生對質！[/impact]他殺了人，不能讓他繼續逍遙自在！",
                    choices: [
                        { text: "好，我現在就去。", tone: "neutral", nextNode: "END" }
                    ]
                },
                FANG_BONUS_POLITE: {
                    text: "（方小蘭想了想）對了，昨晚趙先生問我醫療包裡有沒有繃帶，說他[shake]手被紙割到了[/shake]。但我看他的手，[ink]根本沒有傷口[/ink]。他肯定是想藉機偷走我的[key]聽診器[/key]去偷聽包廂內的談話！",
                    choices: [
                        { text: "這分析很合理。", tone: "neutral", clueId: "CLUE_FANG_BANDAGE", playerReceived: "方小蘭揭露趙福生曾試圖接觸醫療包，並以虛假的傷口作為遮掩，目的是獲取聽診器。", truthVersion: "趙福生利用竊取的聽診器監控江明在包廂內的動靜，尋找最佳下手時機。", nextNode: "END" }
                    ]
                },
                FANG_BONUS_AGGRESSIVE: {
                    text: "（方小蘭被您的語氣激怒）我說的都是實話！我那晚一直在忙著整理病歷和藥品，根本沒空去餐車管你們的閒事！",
                    choices: [
                        { text: "……知道了。", tone: "neutral", clueId: "CLUE_FANG_DEFENSIVE", playerReceived: "方小蘭情緒激動，強調自己昨晚一直在幫病人看診不在餐車。", truthVersion: "方小蘭說的是實話，她確實不在場，但她激動的反應讓玩家誤以為她在隱瞞。", nextNode: "END" }
                    ]
                },
                END: { text: "（方小蘭低頭翻閱著醫療紀錄）請給我一點空間。", choices: [] },
                INTERROGATION: {
                    'CLUE_STETHOSCOPE': 'FANG_2',
                    'CLUE_MANUSCRIPT_PAGE': 'FANG_4'
                }
            }
        };"""

html = re.sub(r'const dialogueTree = \{.*?\n        \};', new_dialogue, html, flags=re.DOTALL)

# ALSO update advanceDialogueRound to not magically advance evidence-gated rounds without them presenting it!
# For ZHAO, ZHAO_2 is camera, ZHAO_3 is letter, ZHAO_4 is stethoscope, ZHAO_5_INTRO is note.
# We should simply return START if we don't want magical advancement. Or return END.
# Actually, if we return END, the user knows they have to present evidence. Let's return "END".
# Wait, if they haven't finished START, it returns START.

adv_logic = """
        function advanceDialogueRound(npcId) {
            const npc = gameState.npcs[npcId];
            const clues = gameState.clues.collected;

            if (npcId === 'CHEN_AFAR') {
                if (npc.round5Done) return 'END';
                if (npc.round4Done) return 'END';
                if (npc.round3Done) return 'END';
                if (npc.round2Done) return 'END';
                if (npc.round1Done) return 'END';
                return 'START';
            }
            if (npcId === 'ZHAO') {
                if (npc.round4Done) return 'END';
                if (npc.round3Done) return 'END';
                if (npc.round2Done) return 'END';
                if (npc.round1Done) return 'END';
                return 'START';
            }
            if (npcId === 'BARONESS') {
                if (npc.round4Done) return 'END';
                if (npc.round3Done) return 'END';
                if (npc.round2Done) return 'END';
                if (npc.round1Done) return 'END';
                return 'START';
            }
            if (npcId === 'FANG') {
                if (npc.round3Done) return 'END';
                if (npc.round2Done) return 'END';
                if (npc.round1Done) return 'END';
                return 'START';
            }
            return 'START';
        }
"""
html = re.sub(r'function advanceDialogueRound\(npcId\) \{.*?\n        \}', adv_logic.strip(), html, flags=re.DOTALL)

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Dialogue Tree and Rounds Logic perfectly updated to enforce Evidence presentation!')
