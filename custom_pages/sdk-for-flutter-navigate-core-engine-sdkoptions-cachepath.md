---
title: "cachePath property"
slug: "sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- cachePath.html -->


<div>
<h1>cachePath property</h1></div>

        
        String
        cachePath
<div class="features">getter/setter pair</div>


<p>Path to be used for caching purposes. It should be a path to the desired location where the application has read/write permissions.
The path can be on internal or external storage.
By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:</p>
<p><code>&lt;Application_Home&gt;/Library/Caches</code> for iOS and <code>Context.getCacheDir().getPath()</code> for Android.
If an absolute path is set, it will be used instead.
If a relative path is set then directory
<code>&lt;Application_Home&gt;/Library/Caches</code> for iOS and <code>Context.getCacheDir().getPath()</code> for Android is used as parent path.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String cachePath;</code></pre>

 



</div>
`
}</HTMLBlock>
