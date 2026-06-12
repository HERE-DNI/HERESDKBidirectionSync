---
title: "save abstract method"
slug: "sdk-for-flutter-navigate-navigation-gpxdocument-save"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- save.html -->


<div>
<h1>save abstract method</h1></div>

bool
save(<ol class="parameter-list single-line"> <li>String gpxFilePath</li>
</ol>)

      

    

<p>Saves the document to a file.</p>
<p>For saving the <a href="/sdk-for-flutter-navigate-navigation-gpxdocument-tracks">GPXDocument.tracks</a> modification before writing to a file, use <a href="/sdk-for-flutter-navigate-navigation-gpxtrackwriter-class">GPXTrackWriter</a>.</p>
<ul>
<li><code>gpxFilePath</code> The file path where the GPX document will be saved.</li>
</ul>
<p>Returns <code>bool</code>. <code>True</code> if the document has been saved successfully.
<code>False</code> if an error has been happened during saving.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool save(String gpxFilePath);</code></pre>

 



</div>
`
}</HTMLBlock>
