---
title: "sdkUsageStats property"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-sdkusagestats"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- sdkUsageStats.html -->


<div>
<h1>sdkUsageStats property</h1></div>
<section id="getter">

List&lt;<a href="/sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a>&gt;
sdkUsageStats


<p>Gets a list of usage statistics for all available HERE SDK features.
<a href="/sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a> has cache and persistent storage. Reads from the persistent storage happen on <code>SDKNativeEngine</code> creation step.
Writes to persistent storage happen by reaching internal limit (amount of upload bytes, by default is 50KB).</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Gets a list of usage statistics for all available HERE SDK features.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;UsageStats&gt; get sdkUsageStats;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
