---
title: "customEngineOptions property"
slug: "sdk-for-flutter-explore-core-engine-sdkoptions-customengineoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- customEngineOptions.html -->


<div>
<h1>customEngineOptions property</h1></div>

        
        Map&lt;<a href="/sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a>, <a href="/sdk-for-flutter-explore-core-engine-engineoptions-class">EngineOptions</a>&gt;
customEngineOptions
<div class="features">getter/setter pair</div>


<p>Set custom options for SDK Engines. This includes:</p>
<ul>
<li><code>custom_base_url</code>: Allows engines to use custom base URLs for alternative services.
By default, the available endpoints use HERE backend endpoints.
If unsupported base URLs are specified, the related features will become non-functional.
Please contact your HERE representative to learn about possible custom base URL usage options.</li>
<li><code>custom_authentication_mode</code>: Enables bearer authentication mode for engines,
which adds or omits the header ("Authorization", "Bearer $Token") to each
online request made by the module the object is added to.
The token (if used) can be provided directly or retrieved via key/secret
from a dedicated backend.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;EngineBaseURL, EngineOptions&gt; customEngineOptions;</code></pre>

 



</div>
`
}</HTMLBlock>
