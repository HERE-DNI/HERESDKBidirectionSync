---
title: "cameraBehavior property"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-camerabehavior"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- cameraBehavior.html -->


<div>
<h1>cameraBehavior property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a>?
cameraBehavior


<p>Camera behavior which defines how the <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> handles the camera.
Setting <code>null</code> disables any camera behavior with the result that the camera does not follow
the current location and keeps the last active camera state, i.e., current zoom and tilt.
Furthermore, when <code>null</code> is set map gestures can be used again to freely pan and zoom
the map. In opposition, when a camera behavior is defined, then the map cannot be panned and
zoomed by the user.
The default value is an instance of <a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class">FixedCameraBehavior</a>.
Gets the currently set camera behavior.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">CameraBehavior? get cameraBehavior;</code></pre>

</section>
<section id="setter">

void
cameraBehavior=(<a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a>? value)


<p>Camera behavior which defines how the <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> handles the camera.
Setting <code>null</code> disables any camera behavior with the result that the camera does not follow
the current location and keeps the last active camera state, i.e., current zoom and tilt.
Furthermore, when <code>null</code> is set map gestures can be used again to freely pan and zoom
the map. In opposition, when a camera behavior is defined, then the map cannot be panned and
zoomed by the user.
The default value is an instance of <a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class">FixedCameraBehavior</a>.
Sets how the VisualNavigator handles the camera.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set cameraBehavior(CameraBehavior? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
