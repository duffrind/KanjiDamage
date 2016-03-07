import os
from urllib.parse import quote

file_list = []

for root,dirs,files in os.walk("./init/"):
  for ffile in files:
    if ffile.endswith(".html"):
      if root[-1] != '/':
        root += '/'
      if not all(ord(char) < 128 for char in ffile):
        new_name = ''
        for char in ffile:
          if ord(char) < 128:
            new_name += char
        file_list.append((ffile,new_name))
        file_list.append((quote(ffile,safe=''),new_name))
        os.rename(root+ffile,root+new_name)


for root, dirs, files in os.walk("./init/"):
  for fffile in files:
    if fffile.endswith(".html"):
      if root[-1] != '/':
        root += '/'
      f = open(root+fffile, 'r+')
      text = f.read()
      for title, new_title in file_list:
        text = text.replace(title,new_title)
      text = text.replace(r'''<script>
  //<![CDATA[
    (function(d, s, id) {
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) return;
      js = d.createElement(s); js.id = id;
      js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=122407024560957";
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
  //]]>
</script>''','')
      dots = ('.' * (root.count('/') - 1)) + '/'
      text = text.replace('http://www.kanjidamage.com/', dots)
      text = text.replace(r"""<!--[if lt IE 9]>
<script src="http://html5shim.googlecode.com/svn/trunk/html5.js" type="text/javascript"></script>
<![endif]-->
<link href='http://fonts.googleapis.com/css?family=Londrina+Solid' rel='stylesheet' type='text/css'>""",'')
      text = text.replace(r"""<script>
  //<![CDATA[
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-12423647-1']);
    _gaq.push(['_trackPageview']);
    
    (function() {
      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
  //]]>
</script>
          <script type='text/javascript'>
            var mpq = [];
            mpq.push(["init", "c9b49675ff5c8dd8c73e0b5c73987bfc"]);
            (function(){var b,a,e,d,c;b=document.createElement("script");b.type="text/javascript";b.async=true;b.src=(document.location.protocol==="https:"?"https:":"http:")+"//api.mixpanel.com/site_media/js/api/mixpanel.js";a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(b,a);e=function(f){return function(){mpq.push([f].concat(Array.prototype.slice.call(arguments,0)))}};d=["track","track_links","track_forms","register","register_once","identify","name_tag","set_config"];for(c=0;c<d.length;c++){mpq[d[c]]=e(d[c])}})();
          </script>
<script type='text/javascript'>try {mpq.push(["register", {}]);} catch(err) {}</script>""",'')
      text = text.replace(r"""<li><a href="http://kanjidamage.fr.yuku.com/forums/2/kanjidamage-forums">Forum</a></li>""",'')
      text = text.replace(r"""<div class='pull-right'>
<div class="fb-like pull-left" data-href="http://www.facebook.com/kanjidamage" data-send="false" data-layout="button_count" data-width="100" data-show-faces="false" data-colorscheme="dark" style="margin: 10px 10px 0"></div>
<form accept-charset="UTF-8" action="/kanji/search" class="navbar-search pull-right" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
<input class="search-query" id="q" name="q" placeholder="Search" type="text" />
</form>

</div>""",'')
      text = text.replace(r"""<div class='span2'><script async src="http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Skyscraper -->
<ins class="adsbygoogle"
     style="display:inline-block;width:160px;height:600px"
     data-ad-client="ca-pub-3566358308304401"
     data-ad-slot="7475140170"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>""",'')
      text = text.replace(r"""<h3>Improved Search!</h3>
There is a search box is in the menu bar (upper right), and here:
<p></p>
<form accept-charset="UTF-8" action="/kanji/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
<table>
<tr>
<td><input id="q" name="q" type="text" /></td>
<td>&nbsp;</td>
<td style='vertical-align: top;'><input name="commit" type="submit" value="Lookup Kanji" /></td>
</tr>
</table>
Previously, you could look up a kanji by searching on the English meaning, or the original kanji.
You can now search kanji by entering the phonetic transliteration, either onyomi or kunyomi.
For example, searching on 'sun' will find two kanji which mean 'sun', two with matching kunyomi
(suna, sunareru), and one with an onyomi of SUN. The search box also accepts kana;
searching on すな will find すな and すなれる.
</form>

<h2>Support us!</h2>
<p>
Please help us improve the accuracy, site design, and Yo Mama jokes
<a href='http://kanjidamage.fr.yuku.com/forums/2/kanjidamage-forums'>here.</a>
</p>
<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----
">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>

<form action="http://mobalean.us2.list-manage1.com/subscribe/post?u=d52315a0a5beaeefbaaa6dfcb&amp;id=3c955226f3" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="form-inline" target="_blank">
    <label for="mce-EMAIL">Get the latest Kanji Damage news!</label>
    <input type="email" value="" name="EMAIL" class="input-medium" id="mce-EMAIL" placeholder="email address" required>
    <input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button">
</form>

</div>
<div class='span4'>
<script async src="http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Skyscraper -->
<ins class="adsbygoogle"
     style="display:inline-block;width:160px;height:600px"
     data-ad-client="ca-pub-3566358308304401"
     data-ad-slot="7475140170"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

<div class="fb-like-box" data-href="https://www.facebook.com/pages/KANJIDAMAGE/344413899661" data-width="300" data-show-faces="true" data-border-color="white" data-stream="false" data-header="false"></div>""",'')
      text = text.replace(r"""<div class='container'><div class="adsense">
<script async src="http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Leaderboard -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-3566358308304401"
     data-ad-slot="1568207378"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>""",'')
      f.seek(0)
      f.write(text)
      f.truncate()
      f.close()