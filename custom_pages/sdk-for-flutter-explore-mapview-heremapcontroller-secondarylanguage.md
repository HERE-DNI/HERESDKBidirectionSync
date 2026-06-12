---
title: "secondaryLanguage property"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-secondarylanguage"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- secondaryLanguage.html -->


<div>
<h1>secondaryLanguage property</h1></div>
<section id="getter">

<a href="/sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?
secondaryLanguage


<p>The code of desired secondary map display language.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static LanguageCode? get secondaryLanguage =&gt; $prototype.secondaryLanguage;</code></pre>

</section>
<section id="setter">

void
secondaryLanguage=(<a href="/sdk-for-flutter-explore-core-languagecode">LanguageCode</a>? languageCode)


<p>Sets the desired secondary map display language for all instances of
MapView to <code>languageCode</code>. Applying a language change causes map to be
redrawn. If the specified language is not supported, local language of the
region will be used. If null, no secondary map language will be used which
is the default behaviour.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void set secondaryLanguage(LanguageCode? languageCode) {
  $prototype.secondaryLanguage = languageCode;
}</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
