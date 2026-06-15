---
title: "AutomotiveCameraBehavior.fromJson constructor"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-automotivecamerabehavior-fromjson"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AutomotiveCameraBehavior.fromJson.html -->


<div>
<h1>AutomotiveCameraBehavior.fromJson constructor</h1></div>

AutomotiveCameraBehavior.fromJson(<ol class="parameter-list single-line"> <li>String configJson</li>
</ol>)
    

<p>Creates a new instance of this class configured from a JSON string.</p>
<p>The JSON configuration is validated during construction and applied to the
underlying <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class">TrackingCameraBehavior</a> and <a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-class">AreaCameraBehavior</a> instances.</p>
<ul>
<li><code>configJson</code> A JSON string containing automotive camera configuration settings.</li>
</ul>
<p>Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a> when the JSON is malformed or contains
invalid values.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory AutomotiveCameraBehavior.fromJson(String configJson) =&gt; $prototype.fromJson(configJson);</code></pre>

 



</div>
`
}</HTMLBlock>
