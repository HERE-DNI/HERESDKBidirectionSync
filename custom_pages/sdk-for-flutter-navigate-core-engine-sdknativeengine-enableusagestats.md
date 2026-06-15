---
title: "enableUsageStats abstract method"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-enableusagestats"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enableUsageStats.html -->


<div>
<h1>enableUsageStats abstract method</h1></div>

void
enableUsageStats(<ol class="parameter-list single-line"> <li>bool enabled</li>
</ol>)

      

    

<p>Enable or disable <a href="sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a> for the HERE SDK.</p>
<p>Defaults to disabled (false). When enabled, <code>SDKNativeEngine.getSdkUsageStats()</code>
returns actual online data consumption. Note that the flag does not cancel pending requests.
<a href="sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a> can be enabled or disabled at any time.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>enabled</code> True, if UsageStats are enabled.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void enableUsageStats(bool enabled);</code></pre>

 



</div>
`
}</HTMLBlock>
