---
title: "makeSharedInstance static method"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-makesharedinstance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- makeSharedInstance.html -->


<div>
<h1>makeSharedInstance static method</h1></div>

Future&lt;void&gt;
makeSharedInstance(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-engine-sdkoptions-class">SDKOptions</a> options</li>
</ol>)

      

    

<p>Makes a new instance of SDKNativeEngine using supplied options and stores it as shared instance
see <a href="/sdk-for-flutter-explore-core-engine-sdknativeengine-sharedinstance">SDKNativeEngine.sharedInstance</a>.</p>
<p>If there was previously shared instance
then it's disposed (see <a href="/sdk-for-flutter-explore-core-engine-sdknativeengine-dispose">SDKNativeEngine.dispose</a>)
before new instance is created.</p>
<ul>
<li><code>options</code> The options for the new engine.</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-explore-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static Future&lt;void&gt; makeSharedInstance(SDKOptions options) =&gt; $prototype.makeSharedInstance(options);</code></pre>

 



</div>
`
}</HTMLBlock>
