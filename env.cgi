#!/usr/bin/env perl

print <<'EOT';
Content-Type: text/html

<head>
  <meta charset="utf-8" />

    <!-- Set the viewport width to device width for mobile -->
      <meta name="viewport" content="width=device-width" />

        <title>Stackato Environment Variables</title>
</head>
<body>
<h1>[ Stackato ] Environment Variables</h1>
<ul>
EOT

print "<li>$_=$ENV{$_}</li>\n" for sort keys %ENV;

print <<'EOT';
</ul>
</body>
</html>
EOT
