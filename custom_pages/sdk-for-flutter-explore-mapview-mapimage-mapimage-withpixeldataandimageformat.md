---
title: "MapImage.withPixelDataAndImageFormat constructor"
slug: "sdk-for-flutter-explore-mapview-mapimage-mapimage-withpixeldataandimageformat"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapImage.withPixelDataAndImageFormat.html -->


<div>
<h1>MapImage.withPixelDataAndImageFormat constructor</h1></div>

MapImage.withPixelDataAndImageFormat(<ol class="parameter-list single-line"> <li>Uint8List pixelData, </li>
<li><a href="sdk-for-flutter-explore-mapview-imageformat">ImageFormat</a> imageFormat</li>
</ol>)
    

<p>Creates a new map image from the provided image data.</p>
<p>Currently only <a href="sdk-for-flutter-explore-mapview-imageformat">ImageFormat.png</a>
is accepted.</p>
<ul>
<li>
<p><code>pixelData</code> Data to be used for the image. The bytes of a PNG image datastream are expected as
defined in <a href="https://www.w3.org/TR/PNG">https://www.w3.org/TR/PNG</a></p>
</li>
<li>
<p><code>imageFormat</code> The format of the image data to be used.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapImage.withPixelDataAndImageFormat(Uint8List pixelData, ImageFormat imageFormat) =&gt; $prototype.withPixelDataAndImageFormat(pixelData, imageFormat);</code></pre>

 



</div>
`
}</HTMLBlock>
