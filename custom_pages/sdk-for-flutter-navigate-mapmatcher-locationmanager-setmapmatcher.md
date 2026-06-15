---
title: "setMapMatcher abstract method"
slug: "sdk-for-flutter-navigate-mapmatcher-locationmanager-setmapmatcher"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMapMatcher.html -->


<div>
<h1>setMapMatcher abstract method</h1></div>

void
setMapMatcher(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a>? mapMatcher</li>
</ol>)

      

    

<p>Sets the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> for exclusive use by <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>.</p>
<p><strong>Threading:</strong> This method is asynchronous and performs the switch in an internal thread of <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>.
<strong>Note:</strong> After calling this method, the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> is owned and used exclusively
by <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a> in its internal processing thread.
Do not use or access the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> elsewhere while it is set.</p>
<ul>
<li><code>mapMatcher</code> The <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> instance to be used exclusively by <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setMapMatcher(MapMatcher? mapMatcher);</code></pre>

 



</div>
`
}</HTMLBlock>
