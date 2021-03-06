import discord

emb = discord.Embed(title="AK-47", description="1949年にソビエト連邦軍が正式採用した自動小銃．", color=0xff8c00)
emb.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/f/f6/AK-47_assault_rifle.jpg")
emb.add_field(name="口径", value="7.62 mm", inline=False)
emb.add_field(name="全長", value="870 mm", inline=False)
emb.add_field(name="重量", value="4,400 g（マガジン付）", inline=False)
emb.add_field(name="発射速度", value="600 発/分", inline=False)
dic = {'AK-47':emb}

emb = discord.Embed(title="FN P90", description="1980年代末にベルギーのFN社が開発したPDW．", color=0x4682b4)
emb.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/s7pli0maIJLFeCseUnUWLHsp6iQxCuhc20VRu1yurCo8QYygHQ__JJNPKyhgQN81BsORW_-dtihXuEJpICaEH_8i0-ULkl_e1ZINFuIK3ATcy48gBLS1S05qug")
emb.add_field(name="口径", value="5.7 mm", inline=False)
emb.add_field(name="全長", value="500 mm", inline=False)
emb.add_field(name="重量", value="3.0 kg（装填時）", inline=False)
emb.add_field(name="発射速度", value="900 発/分", inline=False)
dic['P90'] = emb

emb = discord.Embed(title="H&K MP5", description="1966年にドイツのヘッケラー&コッホ（H&K）社が設計した短機関銃．", color=0x4682b4)
emb.set_thumbnail(url="https://previews.123rf.com/images/snak/snak1305/snak130500559/19950768-9-mm-%E3%81%AE%E7%9F%AD%E6%A9%9F%E9%96%A2%E9%8A%83-mp5-%E3%81%AE%E5%88%86%E9%9B%A2.jpg")
emb.add_field(name="口径", value="9 mm", inline=False)
emb.add_field(name="全長", value="550 mm", inline=False)
emb.add_field(name="重量", value="3.08 kg", inline=False)
emb.add_field(name="発射速度", value="800 発/分", inline=False)
dic['MP5'] = emb

emb = discord.Embed(title="L85A2", description="2001年にイギリスで開発されたアサルトライフル．ヘッケラー&コッホ社（H&K）が改良した．", color=0x4682b4)
emb.set_thumbnail(url="https://previews.123rf.com/images/snak/snak1407/snak140700002/29715825-l85-%E3%81%8C%E7%99%BD%E3%81%84%E8%83%8C%E6%99%AF%E3%81%AB%E5%88%86%E9%9B%A2%E3%81%95%E3%82%8C%E3%81%9F%E3%82%A4%E3%82%AE%E3%83%AA%E3%82%B9%E3%81%AE%E3%82%A2%E3%82%B5%E3%83%AB%E3%83%88%E3%83%A9%E3%82%A4%E3%83%95%E3%83%AB.jpg")
emb.add_field(name="口径", value="5.56 mm", inline=False)
emb.add_field(name="全長", value="785 mm", inline=False)
emb.add_field(name="重量", value="3,820 g（本体のみ）", inline=False)
emb.add_field(name="発射速度", value="610-775 発/分", inline=False)
dic['L85A2'] = emb

emb =discord.Embed(title="レミントンM870", description="1960年代中期にアメリカのレミントン・アームズ社がM31の後継として開発したポンプアクション式散弾銃．", color=0x808080)
emb.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfSvbZNg_oY_mHTPkDRMI-mKN_R9FEi7RB0g&usqp=CAU")
emb.add_field(name="全長", value="946-1,245 mm", inline=False)
emb.add_field(name="重量", value="3.2-3.6 kg", inline=False)
dic['M870'] = emb

emb = discord.Embed(title="M4", description="1994年にアメリカのコルト・ファイヤーアームズ社が開発し，アメリカ軍が採用しているアサルトカービン．", color=0x808080)
emb.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/8/8a/M4_PEO_Soldier.jpg")
emb.add_field(name="口径", value="5.56 mm", inline=False)
emb.add_field(name="全長", value="850.9 mm", inline=False)
emb.add_field(name="重量", value="2,680 g（弾倉を除く）", inline=False)
emb.add_field(name="発射速度", value="700-900 発/分", inline=False)
dic['M4'] = emb

emb = discord.Embed(title="M16A4", description="1996年にアメリカのユージン・ストーナーによって開発されたアメリカ合衆国の小口径自動小銃．M16A4にはピカティニー・レールが採用された．", color=0x808080)
emb.set_thumbnail(url="https://www.military-today.com/firearms/m16a4.jpg")
emb.add_field(name="口径", value="5.56 mm", inline=False)
emb.add_field(name="全長", value="999 mm", inline=False)
emb.add_field(name="重量", value="3,500 g", inline=False)
emb.add_field(name="発射速度", value="900 発/分", inline=False)
dic['M16A4'] = emb
