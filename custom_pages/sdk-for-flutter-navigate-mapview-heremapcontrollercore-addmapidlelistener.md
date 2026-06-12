---
title: "addMapIdleListener abstract method"
slug: "sdk-for-flutter-navigate-mapview-heremapcontrollercore-addmapidlelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapIdleListener.html -->


<div>
<h1>addMapIdleListener abstract method</h1></div>

void
addMapIdleListener(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-mapidlelistener-class">MapIdleListener</a> listener</li>
</ol>)

      

    

<p>Adds a listener for receiving idle state
notifications and notifies it of the current state.</p>
<p>The first notification received is always the state at the time of registration.</p>
<p>The new listener is appended to the set
of <code>HereMap</code> idle listeners as a strong reference.
The caller is responsible for releasing the strong reference by calling
<a href="/sdk-for-flutter-navigate-mapview-heremapcontrollercore-removemapidlelistener">HereMapControllerCore.removeMapIdleListener</a>.</p>
<p>The idle state notifications can occur on an arbitrary thread.</p>
<ul>
<li><code>listener</code> The listener</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addMapIdleListener(MapIdleListener listener);</code></pre>

 



</div>
`
}</HTMLBlock>
