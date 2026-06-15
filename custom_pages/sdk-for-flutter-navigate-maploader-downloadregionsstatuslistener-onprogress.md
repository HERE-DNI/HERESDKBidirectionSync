---
title: "onProgress abstract method"
slug: "sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-onprogress"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onProgress.html -->


<div>
<h1>onProgress abstract method</h1></div>

void
onProgress(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a> region, </li>
<li>int percentage</li>
</ol>)

      

    

<p>Called multiple times to indicate the download progress for each requested region
individually.</p>
<p>Invoked on the main thread.</p>
<ul>
<li>
<p><code>region</code> Represents an id of region status update is related to.</p>
</li>
<li>
<p><code>percentage</code> Represents a percentage of data which has been downloaded for particular
region.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onProgress(RegionId region, int percentage);</code></pre>

 



</div>
`
}</HTMLBlock>
