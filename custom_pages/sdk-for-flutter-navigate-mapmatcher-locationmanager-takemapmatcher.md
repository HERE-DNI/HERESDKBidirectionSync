---
title: "takeMapMatcher abstract method"
slug: "sdk-for-flutter-navigate-mapmatcher-locationmanager-takemapmatcher"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- takeMapMatcher.html -->


<div>
<h1>takeMapMatcher abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a>?
takeMapMatcher()

      

    

<p>Retrieves and removes the <a href="/sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> from <a href="/sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>.</p>
<p><strong>Note:</strong> After calling this method, <a href="/sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a> will no longer use the <a href="/sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> at all.
the caller regains full ownership and responsibility for the <a href="/sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a>.</p>
<p>Returns <a href="/sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher?</a>. The <a href="/sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> instance previously set, or <code>null</code> if none was set.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMatcher? takeMapMatcher();</code></pre>

 



</div>
`
}</HTMLBlock>
