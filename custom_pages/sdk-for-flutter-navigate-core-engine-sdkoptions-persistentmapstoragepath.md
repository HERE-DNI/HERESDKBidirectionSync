---
title: "persistentMapStoragePath property"
slug: "sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- persistentMapStoragePath.html -->


<div>
<h1>persistentMapStoragePath property</h1></div>

        
        String
        persistentMapStoragePath
<div class="features">getter/setter pair</div>


<p>Path to store persistent map data. This should be the a path to the desired location for which the application has read/write permissions.
The path can be on internal or external storage.
By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:</p>
<p><code>Application Library directory</code> for iOS and <code>Context.getFilesDir().getPath()</code> for Android.
If an absolute path is set, it will be used instead.
If a relative path is set then directory
<code>Application Library directory</code> for iOS and <code>Context.getFilesDir().getPath()</code> for Android is used as parent path.
<strong>Note</strong>: Offline maps stored at <code>&lt;persistent_map_storage_path&gt;/v1/&lt;access_key_id&gt;/ocm-map/</code>, where <code>&lt;access_key_id&gt;</code> is
taken from <code>SDKOptions.authenticationMode</code>.
When <code>SDKOptions</code> initialized with <code>AuthenticationMode.withToken</code> or <code>AuthenticationMode.withExternal</code>, then <code>&lt;access_key_id&gt;</code> left empty.</p>
<p>Note: If the persistent map storage location has the read only permission, then the <a href="/sdk-for-flutter-navigate-core-engine-sdkoptions-datapath">SDKOptions.dataPath</a> must be configured.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String persistentMapStoragePath;</code></pre>

 



</div>
`
}</HTMLBlock>
