---
title: "setIndexOptions static method"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-setindexoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setIndexOptions.html -->


<div>
<h1>setIndexOptions static method</h1></div>

<a href="/sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a>?
setIndexOptions(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> sdkEngine, </li>
<li><a href="/sdk-for-flutter-navigate-search-offlinesearchindexoptions-class">OfflineSearchIndexOptions</a> options, </li>
<li><a href="/sdk-for-flutter-navigate-search-offlinesearchindexlistener-class">OfflineSearchIndexListener</a> listener</li>
</ol>)

      

    

<p>Enables or disables indexing.</p>
<p>When indexing is enabled, HERE SDK will create a detailed index over persistent
map data and update it as needed.
A detailed index enables finding data faster and over entire persistent map.
Creating an index takes time, but usually no more than a few seconds up to a couple of
minutes, depending on persistent map size.
As the feature is improved, the indexing time will improve.
Also please note that this is a heavy processing task.
The stored index increases the space taken by offline maps by around 2-5%.
This may also improve in future versions.</p>
<p>Indexing is disabled by default.
If you want it enabled, make sure to call setIndexOptions with <code>OfflineSearchIndex.Options.enabled</code> as <code>true</code> before
any operations in <code>MapDownloader</code> or <code>MapUpdater</code> that modify the persistent map.
Calling setIndexOptions may also create or remove map index to match the previously
installed map regions. If the matching index for installed map regions is found, then
indexing is skipped.
While a new index is being created, <code>OfflineSearchEngine</code> functionality can still be used.
However, without a valid index in place yet, it operates as though indexing is disabled.
If <code>SDKNativeEngine</code> is disposed during indexing (for example, by closing the app),
the indexing is cancelled. Recreating <code>SDKNativeEngine</code> and enabling indexing will
ensure that index is created.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>sdkEngine</code> Indexing is enabled and disabled per SDKNativeEngine instance.
The index is created inside the related <a href="/sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>.</p>
</li>
<li>
<p><code>options</code> Sets indexing options.</p>
</li>
<li>
<p><code>listener</code> The listener that will receive updates about indexing process.
When <code>OfflineSearchIndex.Options.enabled</code> is true, SDK would store listener and the listener will receive updates
about indexing progress every time it is performed.
When <code>OfflineSearchIndex.Options.enabled</code> is false, SDK would report indexing removal progress to the listener
one last time and remove storage of listener.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError?</a>. An error in case there was one.</p>
<p>It's <code>null</code> if the indexing listener could be
configured successfully.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static OfflineSearchIndexError? setIndexOptions(SDKNativeEngine sdkEngine, OfflineSearchIndexOptions options, OfflineSearchIndexListener listener) =&gt; $prototype.setIndexOptions(sdkEngine, options, listener);</code></pre>

 



</div>
`
}</HTMLBlock>
