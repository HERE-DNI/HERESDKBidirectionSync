---
title: "takeScreenshot abstract method"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-takescreenshot"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- takeScreenshot.html -->


<div>
<h1>takeScreenshot abstract method</h1></div>

void
takeScreenshot(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-takescreenshotcallback">TakeScreenshotCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously retrieves a screenshot of the map view.</p>
<p>Note that on Android devices this may not work when the map view is currently not visible,
for example, when an application is running in background and onPause() was called. On iOS
devices the GPU cannot be used when running in background and taking a screenshot is
therefore not possible when the map view is not visible.</p>
<p>The image is returned in a Dart ImageInfo object. The image itself can be accessed from
the ImageInfo.image member and its dimensions from the ImageInfo.image.width and the
ImageInfo.image.height members. These are represented as physical pixels, not device
independent pixels.</p>
<p>If a Flutter Image widget is desired, it can be created thus:</p>
<p>final ByteData byteData = await imageInfo.image.toByteData(format: ui.ImageByteFormat.png);
Image widget = Image.memory(byteData.buffer.asUint8List());</p>
<p><code>callback</code> Completion handler called when the screenshot is completed</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void takeScreenshot(TakeScreenshotCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
