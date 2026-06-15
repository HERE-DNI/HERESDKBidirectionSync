---
title: "searchByCoordinates abstract method"
slug: "sdk-for-flutter-navigate-search-w3wsearchengine-searchbycoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByCoordinates.html -->


<div>
<h1>searchByCoordinates abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
searchByCoordinates(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> coordinates, </li>
<li>String? language, </li>
<li><a href="sdk-for-flutter-navigate-search-w3wsearchcallback">W3WSearchCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to search for a <a href="sdk-for-flutter-navigate-search-w3wsquare-class">W3WSquare</a>, which includes
the 3 word address, that corresponds to the given coordinates.</p>
<ul>
<li>
<p><code>coordinates</code> The coordinates where to search.</p>
</li>
<li>
<p><code>language</code> A supported 3 word address language as an ISO 639-1 2 letter code.
For Bosnian-Croatian-Montenegrin-Serbian use "oo". Defaults to "en" (English).</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that can be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByCoordinates(GeoCoordinates coordinates, String? language, W3WSearchCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
