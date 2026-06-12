---
title: "downloadFile abstract method"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-downloadfile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- downloadFile.html -->


<div>
<h1>downloadFile abstract method</h1></div>

List&lt;Uint8List&gt;
downloadFile(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-mapdata-filereference-class">FileReference</a>&gt; fileReferences, </li>
<li><a href="/sdk-for-flutter-navigate-mapdata-downloadingfileoptions-class">DownloadingFileOptions</a> downloadingOptions</li>
</ol>)

      

    

<p>Synchronously load the optional image providing guidance of a directed or non directed segment.</p>
<ul>
<li>
<p><code>fileReferences</code> Provides information for a file reference.</p>
</li>
<li>
<p><code>downloadingOptions</code> Provides information regarding downloading configuration.</p>
</li>
</ul>
<p>Returns <code>List&lt;Uint8List&gt;</code>. Requested data of a segment.</p>
<p>Throws <a href="/sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class">MapDataLoaderExceptionException</a>. Specifies reason, why list of data of a segment is not returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;Uint8List&gt; downloadFile(List&lt;FileReference&gt; fileReferences, DownloadingFileOptions downloadingOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
