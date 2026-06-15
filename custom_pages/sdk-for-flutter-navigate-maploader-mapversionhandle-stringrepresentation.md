---
title: "stringRepresentation abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapversionhandle-stringrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- stringRepresentation.html -->


<div>
<h1>stringRepresentation abstract method</h1></div>

String
stringRepresentation(<ol class="parameter-list single-line"> <li>String separator</li>
</ol>)

      

    

<p>Returns a string representation of the map version in the format
"[cache-version][separator][offline-maps-version], [japan-cache-version][separator][japan-offline-maps-version]",
which can be obtained via <code>sdk.maploader.MapUpdater</code>.</p>
<ul>
<li><code>separator</code> Separator being used between elements of the map version.
In case map version has single element to it, separator is not used.
<code>none</code> token is used, when it is not possible to determine the version of the map.</li>
</ul>
<p>Examples:</p>
<ul>
<li>separator=", " possible result is "8.10, 9.10"</li>
<li>separator="."  possible result is "8.10.9.10"</li>
<li>separator="; " possible result is "8.10; 9.10"</li>
<li>separator="; " possible result is "8.10"</li>
</ul>
<p>Returns <code>String</code>. A string representation of the map version in the format</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String stringRepresentation(String separator);</code></pre>

 



</div>
`
}</HTMLBlock>
