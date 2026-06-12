---
title: "dataPath property"
slug: "sdk-for-flutter-explore-core-engine-sdkoptions-datapath"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- dataPath.html -->


<div>
<h1>dataPath property</h1></div>

        
        String
        dataPath
<div class="features">getter/setter pair</div>


<p>Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.</p>
<p><strong>Note:</strong> For common use cases, prefer <a href="/sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>, or keep the default paths. Use <code>dataPath</code> only as a fallback if <a href="/sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> is not writable, for example, when you have an agreement with HERE to flash data at factory time.</p>
<p>By default, this returns an empty string. In this case, the same path as <a href="/sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> will be used.
If an absolute path is set, it will be used instead.
If a relative path is set then directory
<code>Application Library directory</code> for iOS and <code>Context.getFilesDir().getPath()</code> for Android is used as parent path.
Application must have read/write permissions to the given desired path.
It is recommended that the application has exclusive access to this path.
Avoid using shared or public directories such as <code>Download</code> or <code>Documents</code>.
Using such directories may cause certain HERE SDK features to behave with limitations.
For example, index creation for offline search may fail or not function as expected.
It is recommended not to use the application cache paths like
<code>&lt;Application_Home&gt;/Library/Caches</code> for iOS and <code>Context.getCacheDir().getPath()</code> for Android, since operating system manages data in this location
and data can be deleted if the device is low on storage space, which will result in application malfunction.
The path can be on internal or external storage. The internal storage is recommended due to the file I/O speed.
Note:
If the <a href="/sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> is writable, <code>dataPath</code> can be left empty.
If the <a href="/sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> is not writable, <code>dataPath</code> must be set and also be writable. Note that <code>dataPath</code> is used to store essential HERE SDK data.</p>
<p><strong>Important:</strong>
There is no automatic migration of stored data between the <a href="/sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> and the <code>dataPath</code>. For ease of management,
it's recommended to set the persistence path as writable and ignore <code>dataPath</code>.
If <code>dataPath</code> is set differently from the <a href="/sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>, some data that would typically be saved in the <a href="/sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> will now be saved to <code>dataPath</code>.
If <code>dataPath</code> is set and later unset, any data stored there will remain inaccessible and will not be migrated back.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String dataPath;</code></pre>

 



</div>
`
}</HTMLBlock>
