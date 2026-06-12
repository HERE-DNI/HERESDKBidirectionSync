---
title: "setAppender static method"
slug: "sdk-for-flutter-navigate-core-engine-logcontrol-setappender"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setAppender.html -->


<div>
<h1>setAppender static method</h1></div>

void
setAppender(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-engine-loglevel">LogLevel</a> level, </li>
<li>String path</li>
</ol>)

      

    

<p>Sets a custom log appender that will write SDK log messages to a file.</p>
<p>This overwrites a previous custom log appender set by user.
Note, that setting the custom appender does not disable logging to the console made by SDK,
in order to do that use <a href="/sdk-for-flutter-navigate-core-engine-logcontrol-disableloggingtoconsole">LogControl.disableLoggingToConsole</a> API.</p>
<ul>
<li>
<p><code>level</code> Log level.</p>
</li>
<li>
<p><code>path</code> Absolute path to a file that the application has read/write permissions.</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-core-engine-logcontrolinvalidpathexceptionexception-class">LogControlInvalidPathExceptionException</a>. <a href="/sdk-for-flutter-navigate-core-engine-logcontrolinvalidpathexceptionexception-class">LogControlInvalidPathExceptionException</a> Indicates that the file path is invalid or not writeable.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void setAppender(LogLevel level, String path) =&gt; $prototype.setAppender(level, path);</code></pre>

 



</div>
`
}</HTMLBlock>
