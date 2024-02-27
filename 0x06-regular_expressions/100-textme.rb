#!/usr/bin/env ruby

matches = ARGV[0].scan(/\[(from|to|flags):(.+?)]/)

new_str = ""

matches.each do |match|
  new_str = new_str + match[1] + ","
end

puts new_str[0..-2]
