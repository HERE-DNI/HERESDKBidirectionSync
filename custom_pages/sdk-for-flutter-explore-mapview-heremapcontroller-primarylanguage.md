---
title: "primaryLanguage property"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-primarylanguage"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- primaryLanguage.html -->


<div>
<h1>primaryLanguage property</h1></div>
<section id="getter">

<a href="/sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?
primaryLanguage


<p>The code of desired primary map display language.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static LanguageCode? get primaryLanguage =&gt; $prototype.primaryLanguage;</code></pre>

</section>
<section id="setter">

void
primaryLanguage=(<a href="/sdk-for-flutter-explore-core-languagecode">LanguageCode</a>? languageCode)


<p>Sets the desired primary map display language for all instances of
MapView to <code>languageCode</code>. Applying a language change causes map to be
redrawn. If null or the specified language is not supported, local
language of the region will be used which is the default behaviour.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void set primaryLanguage(LanguageCode? languageCode) {
  $prototype.primaryLanguage = languageCode;
}</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
