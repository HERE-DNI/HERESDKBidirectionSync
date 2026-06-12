---
title: "attach abstract method"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-attach"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- attach.html -->


<div>
<h1>attach abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
attach(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-search-myplaces-class">MyPlaces</a> dataSource, </li>
<li><a href="/sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a> callback</li>
</ol>)

      

    

<p>Attach data source into SearchEngine instance.</p>
<p>Places from MyPlaces ranked the same
way as places from default source.
New data source replaces old one.
Note: Only OfflineSearchEngine supports search over MyPlaces.</p>
<ul>
<li>
<p><code>dataSource</code> The data source.</p>
</li>
<li>
<p><code>callback</code> The callback to be called when task is completed.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle attach(MyPlaces dataSource, OnTaskCompleted callback);</code></pre>

 



</div>
`
}</HTMLBlock>
