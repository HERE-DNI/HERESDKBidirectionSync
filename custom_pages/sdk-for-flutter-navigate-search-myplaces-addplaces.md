---
title: "addPlaces abstract method"
slug: "sdk-for-flutter-navigate-search-myplaces-addplaces"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addPlaces.html -->


<div>
<h1>addPlaces abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
addPlaces(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-search-geoplace-class">GeoPlace</a>&gt; places, </li>
<li><a href="/sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a> callback</li>
</ol>)

      

    

<p>Adds a list of places to this data source.</p>
<ul>
<li>
<p><code>places</code> Places</p>
</li>
<li>
<p><code>callback</code> The callback to be called when task is completed.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle addPlaces(List&lt;GeoPlace&gt; places, OnTaskCompleted callback);</code></pre>

 



</div>
`
}</HTMLBlock>
