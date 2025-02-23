# Dangerfile

# Check commit message rules
def check_commit_messages(commits)
    commits.each do |commit|
      message = commit.message
      lines = message.split("\n")
  
      if lines[0].length > 50
        fail("Commit title '#{lines[0]}' exceeds 50 characters. Keep it concise!")
      end
  
      if lines.length > 1 && !lines[1].empty?
        fail("Commit message must have an empty line between the title and description.")
      end
  
      if lines.length > 2 && lines[2..-1].join.length < 5
        fail("Commit description must have at least 5 characters.")
      end
  
      lines[2..-1].each do |line|
        if line.length > 72
          fail("Commit description line '#{line}' exceeds 72 characters. Wrap your text!")
        end
      end
    end
  end
  
  check_commit_messages(github.commits)