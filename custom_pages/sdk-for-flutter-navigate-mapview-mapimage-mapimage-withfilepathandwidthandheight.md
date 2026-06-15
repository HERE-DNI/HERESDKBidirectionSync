---
title: "MapImage.withFilePathAndWidthAndHeight constructor"
slug: "sdk-for-flutter-navigate-mapview-mapimage-mapimage-withfilepathandwidthandheight"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapImage.withFilePathAndWidthAndHeight.html -->


<div>
<h1>MapImage.withFilePathAndWidthAndHeight constructor</h1></div>

MapImage.withFilePathAndWidthAndHeight(<ol class="parameter-list single-line"> <li>String filePath, </li>
<li>int width, </li>
<li>int height</li>
</ol>)
    

<p>Creates a new map image from the provided path to the SVG Tiny or PNG image.</p>
<p>Will throw an error if either the height or width equals zero or the path is empty.</p>
<p>Trying to load a file that is not compliant with SVG Tiny or PNG results
in an undefined behavior. In particular, loading SVG that exceeds Tiny SVG
specification may result in an image that exhibits unexpected artifacts.</p>
<p>The caller must ensure that the file remains accessible for the entire duration of its usage by the
SDK. If that cannot be ensured, then it is recommended to either copy the file to a location that
remains accessible for the entire duration of its usage by the SDK or load and pass the file content
to one of the <code>MapImage</code> constructors that creates instances out of image data
(<a href="sdk-for-flutter-navigate-mapview-mapimage-mapimage-withpixeldataandimageformat">MapImage.withPixelDataAndImageFormat</a>, <a href="sdk-for-flutter-navigate-mapview-mapimage-mapimage-withimagedataimageformatwidthandheight">MapImage.withImageDataImageFormatWidthAndHeight</a>).}</p>
<p>Please note that on iOS, file paths that originate, for example from a file picker (like <code>FilePicker</code>)
can be deleted by the system while the application is still running.</p>
<ul>
<li>
<p><code>filePath</code> The path to image file.</p>
</li>
<li>
<p><code>width</code> The width of image in pixels.</p>
</li>
<li>
<p><code>height</code> The height of image in pixels.</p>
</li>
</ul>
<p>Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapImage.withFilePathAndWidthAndHeight(String filePath, int width, int height) =&gt; $prototype.withFilePathAndWidthAndHeight(filePath, width, height);</code></pre>

 



</div>
`
}</HTMLBlock>
