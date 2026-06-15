---
title: "addListener abstract method"
slug: "sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-addlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addListener.html -->


<div>
<h1>addListener abstract method</h1></div>

void
addListener(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class">RasterDataSourceListener</a> listener</li>
</ol>)

      

    

<p>Add listener for receiving state notifications.</p>
<p>The new listener is
appended to the set of data source listeners as a strong reference and will receive only
the notifications occurring after the registration. Caller is responsible for releasing
the strong reference by calling <a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-removelistener">RasterDataSource.removeListener</a>.
The state notifications can occur on an arbitrary thread.</p>
<ul>
<li><code>listener</code> Listener to be added for receiving state notifications.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addListener(RasterDataSourceListener listener);</code></pre>

 



</div>
`
}</HTMLBlock>
