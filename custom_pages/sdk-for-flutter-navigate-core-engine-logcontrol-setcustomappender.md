---
title: "setCustomAppender static method"
slug: "sdk-for-flutter-navigate-core-engine-logcontrol-setcustomappender"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setCustomAppender.html -->


<div>
<h1>setCustomAppender static method</h1></div>

void
setCustomAppender(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-engine-loglevel">LogLevel</a> level, </li>
<li><a href="sdk-for-flutter-navigate-core-engine-logappender-class">LogAppender</a> appender</li>
</ol>)

      

    

<p>Sets a custom log appender to receive log messages from the SDK.</p>
<p>This overwrites a previous custom log appender set by user.
Note, that setting the custom appender does not disable logging to the console made by SDK,
in order to do that use <a href="sdk-for-flutter-navigate-core-engine-logcontrol-disableloggingtoconsole">LogControl.disableLoggingToConsole</a> API.</p>
<ul>
<li>
<p><code>level</code> Log level.</p>
</li>
<li>
<p><code>appender</code> New log appender.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void setCustomAppender(LogLevel level, LogAppender appender) =&gt; $prototype.setCustomAppender(level, appender);</code></pre>

 



</div>
`
}</HTMLBlock>
