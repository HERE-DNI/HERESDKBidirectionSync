---
title: "RepairPersistentMapCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-repairpersistentmapcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RepairPersistentMapCallback.html -->


<div>
<h1>RepairPersistentMapCallback typedef</h1></div>

RepairPersistentMapCallback =
     void Function(<a href="/sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a>? persistentMapRepairError)


<p>A method which is called on the main thread when <a href="/sdk-for-flutter-navigate-maploader-mapdownloader-repairpersistentmap">MapDownloader.repairPersistentMap</a> has been completed.</p>
<p>The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.</p>
<ul>
<li><code>persistentMapRepairError</code> Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef RepairPersistentMapCallback = void Function(PersistentMapRepairError? persistentMapRepairError);</code></pre>

 



</div>
`
}</HTMLBlock>
