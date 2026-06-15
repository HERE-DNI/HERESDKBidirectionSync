---
title: "unpinWidget abstract method"
slug: "sdk-for-flutter-navigate-mapview-heremapcontroller-unpinwidget"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- unpinWidget.html -->


<div>
<h1>unpinWidget abstract method</h1></div>

void
unpinWidget(<ol class="parameter-list single-line"> <li>Widget widget</li>
</ol>)

      

    

<p>Removes a <a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a> from the MapView by specifying the corresponding <code>Widget</code>.
Trying to unpin a widget that was not pinned or has been unpinned before has no effect.
All pinned widgets equal to <code>widget</code> will be removed.</p>
<p><code>widget</code> corresponding to the <a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a> to remove.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void unpinWidget(Widget widget);</code></pre>

 



</div>
`
}</HTMLBlock>
