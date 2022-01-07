# Data Engineer Technical Challenge 💻

Put together a script or program (using any language or technology) that: 

1.) Retrieves "Top Stories" from this parliament data RSS feed endpoint: https://www.europarl.europa.eu/rss/doc/top-stories/en.xml

Sample response:

```
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Top stories - European Parliament</title>
    <link>https://www.europarl.europa.eu/news/en</link>
    <description />
    <language>EN</language>
    <copyright>© European Union, 2021 - EP</copyright>
    <pubDate>Tue, 21 Sep 2021 13:07:46 GMT</pubDate>
    <item>
      <title>Top story - State of the European Union Debate 2021 - Addressing Europeans' concerns</title>
      <link>https://www.europarl.europa.eu/news/en/headlines/priorities/soteu2021</link>
      <description>&lt;img src="https://www.europarl.europa.eu/resources/library/images/20210913PHT12318/20210913PHT12318-ms.jpg" align="left" width="125" hspace="5" vspace="0" /&gt;The most important EU debate of the year, looking at last year’s achievements as well as plans and vision for the future, took place on 15 September.&lt;br /&gt; &lt;br /&gt;Source : &lt;a href="https://www.europarl.europa.eu/privacy-policy/en"&gt;© European Union, 2021 - EP&lt;/a&gt;</description>
      <source url="https://www.europarl.europa.eu/rss/doc/top-stories/en.xml">Top stories - European Parliament</source>
      <category domain="type">Top story</category>
      <pubDate>Mon, 13 Sep 2021 13:03:26 GMT</pubDate>
      <guid isPermaLink="false">TST_TST-2021-09-09-11812_EN</guid>
    </item>
  </channel>
</rss>
```
2.) Outputs a CSV file of the data.

## The Solution Background 💻
 
<p>As per the challenge I have to get the top stories from the RSS data feed. Therefore to resolve this challenge, I had used "PYTHON" scripting language. In the RSS data feed, there is one <em> title </em> tag in the <em> feed </em> and 10 <em> title </em> tags inside the <em> feed entries </em> tags.<br/>
 </p>
 
<h2>📌Assumptions </h2>
<p>* I have taken "Top Stories" sentence from the feed and "Top Story" sentences from entries for the output </p>

## How to use the script 🤔

1. Open the command prompt and type "python --version" command and check whether the python installed or not
2. You have to download the python into your machine (https://www.python.org/downloads/release/python-3101/) (if you don't have the python installed previuosly😁)
3. Once the download completed run the .exe file and you can select to set the path automatically
4. You have to type "pip install feedparser" in the command prompt because in the .py script file I used feedparser package to read and process the RSS feeds
5. You can open the IDLE(Integrated Development and Learning Environment) from the start menu to run the script once the installation process completed
6. To open the .py script file, select the <strong> File </strong> option from the navigation bar and click on <strong> Open </strong> option 
7. To run the .py script file, select <strong> Run </strong> option from the navigation bar and click on <strong> Run Module </strong> option
8. Once you run the script, you can check the results in the .csv file (Feed_Results.csv) which is in the same folder 📑

# Congratulations 🎉🎉🎉
<p> You have run the script successfully😊</p>
