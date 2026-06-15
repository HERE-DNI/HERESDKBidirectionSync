---
title: "repairPersistentMap abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-repairpersistentmap"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- repairPersistentMap.html -->


<div>
<h1>repairPersistentMap abstract method</h1></div>

void
repairPersistentMap(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-repairpersistentmapcallback">RepairPersistentMapCallback</a> callback</li>
</ol>)

      

    

<p>Tries to repair already downloaded regions that are in a corrupted state (see <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus">MapDownloader.getInitialPersistentMapStatus</a>).</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then index will be
rebuilt if existing index does not match with the installed map regions after this operation.
The index is used by <code>OfflineSearchEngine</code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
<ul>
<li><code>callback</code> A callback which receives the result of the repair operation on the main thread.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void repairPersistentMap(RepairPersistentMapCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
